from magclassic import *

GuestEmail('MAGFest food for guests', 'guest_food_restrictions.txt')
GuestEmail('MAGFest hospitality suite information', 'guest_food_info.txt')
StopsEmail('MAGFest Volunteer Food', 'volunteer_food_info.txt',
           lambda a: days_before(7, c.UBER_TAKEDOWN))