from uber.models import Session
from uber.models.types import DefaultColumn as Column, MultiChoice
from uber.config import c

@Session.model_mixin
class Attendee:
    @property
    def num_free_event_shirts(self):
        return 1 if self.badge_type == c.STAFF_BADGE else self.volunteer_event_shirt_eligible

@Session.model_mixin
class GuestMerch:
    extra_merch_time = Column(MultiChoice(c.EXTRA_MERCH_TIME_OPTS))