from magwest import *

# With "MAGWest" as a new event, we find that the phrasing "Want to staff again?"
# doesn't differentiate this event, so we change it to just plain "Want to staff?"
if 'volunteer_again_inquiry' in AutomatedEmail.instances:
    AutomatedEmail.instances['volunteer_again_inquiry'].subject = 'Want to staff {}?'.format(c.EVENT_NAME)

AutomatedEmail(Attendee, '{EVENT_NAME} food for guests', 'guest_food_restrictions.txt',
           lambda a: a.badge_type == c.GUEST_BADGE,
           ident='magwest_guest_food_restrictions',
           sender="MAGFest Staff Suite <chefs@magfest.org>")

AutomatedEmail(Attendee, '{EVENT_NAME} hospitality suite information', 'guest_food_info.txt',
           lambda a: a.badge_type == c.GUEST_BADGE,
           ident='magwest_guest_food_info',
           sender="MAGFest Staff Suite <chefs@magfest.org>")

AutomatedEmail(Attendee, '{EVENT_NAME} Volunteer Food', 'volunteer_food_info.txt',
           lambda a: a.staffing and days_before(7, c.FINAL_EMAIL_DEADLINE),
           ident='magwest_volunteer_food_info',
           sender="MAGFest Staff Suite <chefs@magfest.org>")

AutomatedEmail(Attendee, '{EVENT_NAME} FAQ', 'prefest_faq.html',
               lambda a: a.badge_status == c.COMPLETED_STATUS and days_before(7, c.FINAL_EMAIL_DEADLINE),
               ident='magwest_prefest_faq')

AutomatedEmail(Attendee, '{EVENT_NAME} PC Gaming Survey', 'pc_gaming_survey.html',
           lambda a: c.LAN in a.interests_ints,
           ident='pc_gaming_survey',
           needs_approval=True,
           sender="MAGWest LAN Staff <lan@magwest.org>")

StopsEmail('CORRECTION to the {EVENT_NAME} {EVENT_DATE} Shift Schedule Email', 'shifts/schedule_correction.html',
           lambda a: c.SHIFTS_CREATED and a.weighted_hours,
           when=days_before(1, c.FINAL_EMAIL_DEADLINE),
           ident='volunteer_shift_schedule_correction')
