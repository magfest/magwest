from datetime import timedelta

from uber.automated_emails import AutomatedEmailFixture, MarketplaceEmailFixture, StopsEmailFixture
from uber.config import c
from uber.models import Attendee, AutomatedEmail
from uber.utils import before, days_before, days_after


MarketplaceEmailFixture(
        f'Waitlisted - {c.EVENT_NAME_AND_YEAR}',
        'dealers/waitlisted.txt',
        lambda g: g.status == c.WAITLISTED,
        # query=Group.status == c.WAITLISTED,
        needs_approval=True,
        ident='dealer_reg_waitlisted')

MarketplaceEmailFixture(
        f'About your Declined Dealer\'s Application - {c.EVENT_NAME_AND_YEAR}',
        'dealers/declined.txt',
        lambda g: g.status == c.DECLINED,
        # query=Group.status == c.DECLINED,
        needs_approval=True,
        ident='dealer_reg_declined')


AutomatedEmailFixture(
    Attendee,
    '{EVENT_NAME} food for guests',
    'guest_food_restrictions.txt',
    lambda a: a.badge_type == c.GUEST_BADGE,
    ident='magwest_guest_food_restrictions',
    sender="MAGWest Tea Room <tearoom@magwest.org>")


AutomatedEmailFixture(
    Attendee,
    '{EVENT_NAME} hospitality suite information',
    'guest_food_info.txt',
    lambda a: a.badge_type == c.GUEST_BADGE,
    ident='magwest_guest_food_info',
    sender="MAGWest Tea Room <tearoom@magwest.org>")


AutomatedEmailFixture(
    Attendee,
    '{EVENT_NAME} Volunteer Food',
    'volunteer_food_info.txt',
    lambda a: a.staffing and days_before(7, c.FINAL_EMAIL_DEADLINE),
    ident='magwest_volunteer_food_info',
    sender="MAGWest Tea Room <tearoom@magwest.org>")


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
    sender="MAGWest LAN Staff <lan@magwest.org>")


StopsEmailFixture(
    'CORRECTION to the {EVENT_NAME} ({EVENT_DATE}) Shift Schedule Email',
    'shifts/schedule_correction.html',
    lambda a: c.SHIFTS_CREATED and a.weighted_hours,
    when=days_before(1, c.FINAL_EMAIL_DEADLINE),
    ident='volunteer_shift_schedule_correction')


AutomatedEmailFixture(
    Attendee,
    'Last Chance for MAGWest {EVENT_YEAR} bonus swag!',
    'attendee_swag_promo.html',
    lambda a: a.can_spam and a.badge_status == c.COMPLETED_STATUS and
              a.amount_extra < c.SEASON_LEVEL and days_after(1, a.registered)(),
    when=before(c.EPOCH - timedelta(days=2)),
    sender='MAGWest Merch Team <merch@magwest.org>',
    ident='magwest_bonus_swag_reminder_last_chance')


AutomatedEmail.email_overrides.extend([
    ('panel_accepted', 'subject', f"Approved - {c.EVENT_NAME_AND_YEAR} Panel Application"),
    ('panel_declined', 'subject', f"Declined - {c.EVENT_NAME_AND_YEAR} Panel Application"),
    ('panel_waitlisted', 'subject', f"Waitlisted - {c.EVENT_NAME_AND_YEAR} Panel Application"),
    ('panel_accept_reminder', 'subject', f"Last Chance to Confirm Your Panel - {c.EVENT_NAME_AND_YEAR}"),
    ('panel_scheduled', 'subject', f"Your Panel has been Scheduled - {c.EVENT_NAME_AND_YEAR}")
    ])