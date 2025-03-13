import pytz

from datetime import datetime, timedelta

from uber.custom_tags import datetime_local_filter
from uber.models import Session, Boolean
from uber.models.types import DefaultColumn as Column, MultiChoice
from uber.config import c


@Session.model_mixin
class Attendee:
    @property
    def approved_panel_apps(self):
        return [panel.name for panel in self.submitted_panels if panel.status == c.ACCEPTED]


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