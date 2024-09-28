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


@prereg_validation.Attendee
def attendee_badge_under_13(attendee):
    if c.AT_THE_CON:
        return
    
    if not attendee.is_new and attendee.badge_status not in [c.PENDING_STATUS, c.AT_DOOR_PENDING_STATUS] \
            or attendee.unassigned_group_reg or attendee.valid_placeholder:
        return

    if c.CHILD_BADGE in c.PREREG_BADGE_TYPES and attendee.birthdate and attendee.badge_type == c.ATTENDEE_BADGE and (
            get_age_from_birthday(attendee.birthdate, c.NOW_OR_AT_CON) < 13):
        return ('badge_type', "If you will be 12 or younger at the start of {}, "
                "please select the 12 and Under badge instead of an Attendee badge.".format(c.EVENT_NAME))