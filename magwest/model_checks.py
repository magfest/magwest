from datetime import datetime

from os.path import join

from residue import CoerceUTF8 as UnicodeText
from sqlalchemy.types import Boolean, Date
from uber.api import AttendeeLookup
from uber.config import c, Config
from uber.decorators import cost_property, prereg_validation, presave_adjustment, validation
from uber.menu import MenuItem
from uber.models import Choice, DefaultColumn as Column, Session
from uber.jinja import template_overrides
from uber.utils import localized_now, valid_email, get_age_from_birthday

