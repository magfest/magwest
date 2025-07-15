from wtforms import (BooleanField)

from uber.config import c
from uber.forms import MagForm


@MagForm.form_mixin
class AdminTableInfo:
    night_market = BooleanField(f"This {c.DEALER_TERM} is part of the Night Market.")
