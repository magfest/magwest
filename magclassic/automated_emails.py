from magclassic import *

# With "MAGFest Laboratories" as a new event, we find that the phrasing "Staffing again"
# doesn't differentiate this event, so we remove it.
AutomatedEmail.instances['Want to staff {}?'.format(c.EVENT_NAME)] = AutomatedEmail.instances.pop('Want to staff {} again?'.format(c.EVENT_NAME))

AutomatedEmail(Attendee, 'MAGFest food for guests', 'guest_food_restrictions.txt',
           lambda a: a.badge_type == c.GUEST_BADGE,
           sender="MAGFest Staff Suite <chefs@magfest.org>")
AutomatedEmail(Attendee, 'MAGFest hospitality suite information', 'guest_food_info.txt',
           lambda a: a.badge_type == c.GUEST_BADGE,
           sender="MAGFest Staff Suite <chefs@magfest.org>")
AutomatedEmail(Attendee, 'MAGFest Volunteer Food', 'volunteer_food_info.txt',
           lambda a: a.staffing and days_before(7, c.FINAL_EMAIL_DEADLINE),
           sender="MAGFest Staff Suite <chefs@magfest.org>")
AutomatedEmail(Attendee, 'MAGClassic Check-in Barcode', 'checkin_barcode.html',
               lambda a: a.badge_status == c.COMPLETED_STATUS and days_before(7, c.FINAL_EMAIL_DEADLINE))
AutomatedEmail(Attendee, 'MAGClassic FAQ', 'prefest_faq.html',
               lambda a: a.badge_status == c.COMPLETED_STATUS and days_before(7, c.FINAL_EMAIL_DEADLINE))
