from magclassic import *


@all_renderable(c.PEOPLE)
class Root:
    def tech_requirements(self, session, submitted=None, csrf_token=None):
        attendee = session.admin_attendee()
        if submitted:
            try:
                [item] = [item for item in attendee.dept_checklist_items if item.slug == 'tech_requirements']
            except:
                item = DeptChecklistItem(slug='tech_requirements', attendee=attendee)
            check_csrf(csrf_token)  # since this form doesn't use our normal utility methods, we need to do this manually
            session.add(item)
            raise HTTPRedirect('../dept_checklist/index?message={}', 'Thanks for completing the tech requirements form!')

        return {}