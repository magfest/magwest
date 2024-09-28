import math
from collections import defaultdict
from datetime import timedelta
from pathlib import Path
from markupsafe import Markup

from uber.config import c, Config, dynamic, parse_config
from uber.menu import MenuItem
from uber.utils import localized_now

config = parse_config("magwest", Path(__file__).parents[0])
c.include_plugin_config(config)

@Config.mixin
class ExtraConfig:    
    @property
    def FORMATTED_BADGE_TYPES(self):
        badge_types = []
        if c.AT_THE_CON and self.ONE_DAYS_ENABLED and self.ONE_DAY_BADGE_AVAILABLE:
            badge_types.append({
                'name': 'Single Day',
                'desc': 'Allows access to the convention for today. Can be upgraded to a weekend badge.',
                'value': c.ONE_DAY_BADGE,
                'price': c.ONEDAY_BADGE_PRICE
            })
        badge_types.append({
            'name': 'Attendee',
            'desc': 'Allows access to the convention for its duration.',
            'value': c.ATTENDEE_BADGE,
            'price': c.get_attendee_price()
            })
        if c.GROUPS_ENABLED and c.BEFORE_GROUP_PREREG_TAKEDOWN:
            badge_types.append({
                'name': "Group Leader",
                'desc': Markup(f"Register a group of {c.MIN_GROUP_SIZE} people or more at ${c.GROUP_PRICE} per badge."
                               "<br/><br/><span class='form-text'>Please purchase badges for children 12 and under "
                               "separate from your group.</span>"),
                'value': c.PSEUDO_GROUP_BADGE,
                'price': c.GROUP_PRICE,
            })
        for badge_type in c.BADGE_TYPE_PRICES:
            badge_types.append({
                'name': c.BADGES[badge_type],
                'desc': 'Donate extra to get an upgraded badge with perks.',
                'value': badge_type,
                'price': c.BADGE_TYPE_PRICES[badge_type]
            })
        return badge_types