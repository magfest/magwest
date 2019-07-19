from uber.models import Attendee, Session

@Session.model_mixin
class Attendee:
    @property
    def gets_staff_shirt(self):
        # This is technically just a generic MAGWest shirt, so volunteers are also eligible
        return self.staffing

    @property
    def num_free_event_shirts(self):
        # Volunteers also get to select if they want an event shirt or not, so they do not get a free shirt by default
        return self.num_event_shirts
