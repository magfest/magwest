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
        if self.has_been_accepted and not self.confirmed and not (self.group and self.group.guest):
            if not c.PANELS_INITIAL_CONFIRM_DEADLINE or datetime.now(tz=pytz.UTC) > c.PANELS_INITIAL_CONFIRM_DEADLINE:
                confirm_deadline = timedelta(days=c.PANELS_CONFIRM_DEADLINE)
                return self.accepted + confirm_deadline
            return c.PANELS_INITIAL_CONFIRM_DEADLINE

    @property
    def confirm_deadline_text(self):
        if not c.PANELS_INITIAL_CONFIRM_DEADLINE or datetime.now(tz=pytz.UTC) > c.PANELS_INITIAL_CONFIRM_DEADLINE:
            return f"within {c.PANELS_CONFIRM_DEADLINE} days"
        return f"by {datetime_local_filter(c.PANELS_INITIAL_CONFIRM_DEADLINE)}"