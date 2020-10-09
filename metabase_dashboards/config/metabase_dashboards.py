from __future__ import unicode_literals
from frappe import _

def get_data():

    return [
        {
            "label": _("Accounts"),
            "icon": "octicon octicon-briefcase",
            "items": [
            ]
        },
        {
            "label": _("Human Resources"),
            "icon": "octicon octicon-briefcase",
            "items": [
                {
                    "type": "doctype",
                    "name": "Employee Metrics"
                }
            ]
        },
        {
            "label": _("Projects"),
            "icon": "octicon octicon-briefcase",
            "items": [
            ]
        },
        {
            "label": _("Sales"),
            "icon": "octicon octicon-briefcase",
            "items": [
            ]
        },
        {
            "label": _("Stores"),
            "icon": "octicon octicon-briefcase",
            "items": [
            ]
        },
        {
            "label": _("Support"),
            "icon": "octicon octicon-briefcase",
            "items": [
            ]
        },
    ]