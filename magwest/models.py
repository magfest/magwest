from uber.models import Attendee, Session

@Session.model_mixin
class Attendee:
    @property
    def gets_staff_shirt(self):
        # This is technically just a generic MAGWest shirt, so volunteers are also eligible
        return self.staffing
