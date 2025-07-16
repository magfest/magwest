from datetime import datetime, timedelta

import cherrypy
from collections import defaultdict
from sqlalchemy.orm import subqueryload

from uber.config import c
from uber.custom_tags import datetime_local_filter
from uber.decorators import all_renderable, csv_file, department_id_adapter
from uber.models import Attendee, Shift, RoomAssignment


@all_renderable()
class Root:
    def superstars(self, session):
        counts = {}
        owe_money = {}
        superstars = session.valid_attendees().filter(Attendee.extra_donation >= c.SUPERSTAR_MINIMUM)

        valid_donations_list = c.SUPERSTAR_DONATION_OPTS[1:-1]
        last_index = len(valid_donations_list) - 1
        for index, opt in enumerate(valid_donations_list):
            amt, label = opt
            count_query = session.valid_attendees().filter(Attendee.extra_donation >= amt)
            if index != last_index:
                next_amt, next_label = valid_donations_list[index + 1]
                count_query = count_query.filter(Attendee.extra_donation < next_amt)
            counts[label] = count_query.count()

        for attendee in [a for a in superstars if a.amount_unpaid or not a.active_receipt]:
            owe_money[attendee.id] = attendee.amount_unpaid if attendee.active_receipt else attendee.default_cost
        
        return {
            'attendees': superstars,
            'counts': counts,
            'owe_money': owe_money,
            'total_count': superstars.count(),
        }
    
    @csv_file
    def superstars_csv(self, out, session):
        out.writerow(["Group Name", "Full Name", "Name on ID", "Badge Name", "Badge Type", "Ribbons", "Pre-ordered Merch",
                      "Email", "ZIP/Postal Code", "Checked In"])
        for a in session.valid_attendees().filter(Attendee.extra_donation >= c.SUPERSTAR_MINIMUM):
            out.writerow([a.group_name, a.full_name, a.legal_name, a.badge_printed_name, a.badge_type_label,
                          ' / '.join(a.ribbon_labels), a.amount_extra_label, a.email, a.zip_code,
                          datetime_local_filter(a.checked_in)])
