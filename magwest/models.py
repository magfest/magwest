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