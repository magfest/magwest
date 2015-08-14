from magclassic import *


@all_renderable(c.PEOPLE)
class Root:
    def allotments(self, session, submitted=None, csrf_token=None, **params):
        attendee = session.admin_attendee()
        conf = DeptChecklistConf.instances['treasury']
        if submitted:
            try:
                [item] = [item for item in attendee.dept_checklist_items if item.slug == 'treasury']
            except:
                item = DeptChecklistItem(slug='treasury', attendee=attendee)
            check_csrf(csrf_token)  # since this form doesn't use our normal utility methods, we need to do this manually
            item.comments = render('treasury/allotments.txt', params).decode('utf-8')
            session.add(item)
            raise HTTPRedirect('../dept_checklist/index?message={}', 'Treasury checklist data uploaded')

        return {}
