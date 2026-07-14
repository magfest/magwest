import pytz

from datetime import datetime, timedelta

from uber.custom_tags import datetime_local_filter
from uber.decorators import presave_adjustment
from uber.models import Session, Boolean
from uber.models.types import DefaultColumn as Column, MultiChoice
from uber.config import c
from uber.utils import add_opt, remove_opt


@Session.model_mixin
class Attendee:
    @property
    def approved_panel_apps(self):
        return [panel.name for panel in self.submitted_panels if panel.status == c.ACCEPTED]

    @presave_adjustment
    def set_superstar_ribbon(self):
        if self.extra_donation >= c.SUPERSTAR_MINIMUM and c.SUPERSTAR_RIBBON not in self.ribbon_ints:
            self.ribbon = add_opt(self.ribbon_ints, c.SUPERSTAR_RIBBON)
        elif self.extra_donation < c.SUPERSTAR_MINIMUM and \
                self.orig_value_of('extra_donation') >= c.SUPERSTAR_MINIMUM and c.SUPERSTAR_RIBBON in self.ribbon_ints:
            self.ribbon = remove_opt(self.ribbon_ints, c.SUPERSTAR_RIBBON)

    @property
    def staff_merch_items(self):
        """Used by the merch and staff_merch properties for staff swag."""
        merch = ["Volunteer lanyard"] if self.staffing and self.weighted_hours >= 1 and \
            self.badge_type != c.CONTRACTOR_BADGE else []
        num_staff_shirts_owed = self.num_staff_shirts_owed
        if num_staff_shirts_owed > 0:
            staff_shirts = '{} Staff Shirt{}'.format(num_staff_shirts_owed, 's' if num_staff_shirts_owed > 1 else '')
            if self.shirt_size_marked:
                try:
                    if c.STAFF_SHIRT_OPTS != c.SHIRT_OPTS:
                        staff_shirts += ' [{}]'.format(c.STAFF_SHIRTS[self.staff_shirt])
                    else:
                        staff_shirts += ' [{}]'.format(c.SHIRTS[self.shirt])
                except KeyError:
                    staff_shirts += ' [{}]'.format("Size unknown")
            merch.append(staff_shirts)
        elif self.could_get_staff_shirt and self.shirt_opt_out in [c.STAFF_OPT_OUT, c.ALL_OPT_OUT]:
            merch.append("NO Staff Shirt")

        if self.staffing:
            merch.append('Staffer Info Packet')

        return merch


@Session.model_mixin
class Group:
    night_market = Column(Boolean, default=False)


@Session.model_mixin
class GuestMerch:
    extra_merch_time = Column(MultiChoice(c.EXTRA_MERCH_TIME_OPTS))


@Session.model_mixin
class GuestStagePlot:
    wants_visualist = Column(Boolean, default=False)


@Session.model_mixin
class PanelApplication:
    @property
    def confirm_deadline(self):
        if c.PANELS_CONFIRM_DEADLINE and self.has_been_accepted and not self.confirmed and not (self.group and self.group.guest):
            if not c.PANELS_INITIAL_CONFIRM_DEADLINE or datetime.now(tz=pytz.UTC) > c.PANELS_INITIAL_CONFIRM_DEADLINE:
                confirm_deadline = timedelta(days=c.PANELS_CONFIRM_DEADLINE)
                return self.accepted + confirm_deadline
            return c.PANELS_INITIAL_CONFIRM_DEADLINE

    @property
    def confirm_deadline_text(self):
        if not c.PANELS_CONFIRM_DEADLINE:
            return ''

        if not c.PANELS_INITIAL_CONFIRM_DEADLINE or datetime.now(tz=pytz.UTC) > c.PANELS_INITIAL_CONFIRM_DEADLINE:
            return f"within {c.PANELS_CONFIRM_DEADLINE} days"
        return f"by {datetime_local_filter(c.PANELS_INITIAL_CONFIRM_DEADLINE)}"