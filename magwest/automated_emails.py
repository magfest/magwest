from datetime import timedelta

from uber.automated_emails import AutomatedEmailFixture, BandEmailFixture, StopsEmailFixture
from uber.config import c
from uber.models import Attendee
from uber.utils import before, days_before


AutomatedEmailFixture(
    Attendee,
    '{EVENT_NAME} food for guests',
    'guest_food_restrictions.txt',
    lambda a: a.badge_type == c.GUEST_BADGE,
    ident='magwest_guest_food_restrictions',
    sender="MAGFest Staff Suite <chefs@magfest.org>")

AutomatedEmailFixture(
    Attendee,
    '{EVENT_NAME} hospitality suite information',
    'guest_food_info.txt',
    lambda a: a.badge_type == c.GUEST_BADGE,
    ident='magwest_guest_food_info',
    sender="MAGFest Staff Suite <chefs@magfest.org>")

AutomatedEmailFixture(
    Attendee,
    '{EVENT_NAME} Volunteer Food',
    'volunteer_food_info.txt',
    lambda a: a.staffing and days_before(7, c.FINAL_EMAIL_DEADLINE),
    ident='magwest_volunteer_food_info',
    sender="MAGFest Staff Suite <chefs@magfest.org>")

AutomatedEmailFixture(
    Attendee,
    '{EVENT_NAME} FAQ',
    'prefest_faq.html',
    lambda a: a.badge_status == c.COMPLETED_STATUS and days_before(7, c.FINAL_EMAIL_DEADLINE),
    ident='magwest_prefest_faq')

AutomatedEmailFixture(
    Attendee,
    '{EVENT_NAME} PC Gaming Survey',
    'pc_gaming_survey.html',
    lambda a: c.LAN in a.interests_ints,
    ident='pc_gaming_survey',
    needs_approval=True,
    sender="MAGWest LAN Staff <lan@magwest.org>")

StopsEmailFixture(
    'CORRECTION to the {EVENT_NAME} ({EVENT_DATE}) Shift Schedule Email',
    'shifts/schedule_correction.html',
    lambda a: c.SHIFTS_CREATED and a.weighted_hours,
    when=days_before(1, c.FINAL_EMAIL_DEADLINE),
    ident='volunteer_shift_schedule_correction')
