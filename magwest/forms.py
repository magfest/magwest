from wtforms import (BooleanField)

from uber.config import c
from uber.forms import MagForm


@MagForm.form_mixin
class AdminTableInfo:
    night_market = BooleanField(f"This {c.DEALER_TERM} is part of the Night Market.")


@MagForm.form_mixin
class BaseJobInfo:
    no_slots = HiddenField('')


@MagForm.form_mixin
class JobInfo:
    slots = IntegerField('Slots', default=1)


@MagForm.form_mixin
class JobTemplateInfo:
    min_slots = IntegerField('Minimum # Slots', default=1)

    def no_slots_label(self):
        return ''
    
    def no_slots_desc(self):
        return ""
