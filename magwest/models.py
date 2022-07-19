from uber.models import Session
from uber.models.types import DefaultColumn as Column, MultiChoice
from uber.config import c

@Session.model_mixin
class Attendee:
    @property
    def gets_staff_shirt(self):
        # This is technically just a generic MAGWest shirt, so volunteers are also eligible
        return self.staffing
    
    @property
    def num_free_event_shirts(self):
        return 1 if self.staffing else 0

@Session.model_mixin
class GuestMerch:
    extra_merch_time = Column(MultiChoice(c.EXTRA_MERCH_TIME_OPTS))