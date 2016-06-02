from magclassic import *

AutomatedEmail(Attendee, 'MAGFest food for guests', 'guest_food_restrictions.txt',
           lambda a: a.badge_type == c.GUEST_BADGE,
           sender="MAGFest Staff Suite <chefs@magfest.org>")
AutomatedEmail(Attendee, 'MAGFest hospitality suite information', 'guest_food_info.txt',
           lambda a: a.badge_type == c.GUEST_BADGE,
           sender="MAGFest Staff Suite <chefs@magfest.org>")
AutomatedEmail(Attendee, 'MAGFest Volunteer Food', 'volunteer_food_info.txt',
           lambda a: a.staffing and days_before(7, min(c.UBER_TAKEDOWN, c.EPOCH)),
           sender="MAGFest Staff Suite <chefs@magfest.org>")
AutomatedEmail(Attendee, 'MAGClassic Check-in Barcode', 'checkin_barcode.html',
               lambda a: a.badge_status == c.COMPLETED_STATUS and days_before(7, min(c.UBER_TAKEDOWN, c.EPOCH)))
AutomatedEmail(Attendee, 'MAGClassic FAQ', 'prefest_faq.html',
               lambda a: a.badge_status == c.COMPLETED_STATUS and days_before(7, min(c.UBER_TAKEDOWN, c.EPOCH)))
