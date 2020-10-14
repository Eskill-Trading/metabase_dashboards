from __future__ import unicode_literals
from frappe import _

def get_data():

    return [
        {
            "label": _("Accounts"),
            "icon": "octicon octicon-briefcase",
            "items": [
				{
					"type": "page",
					"name": "gross-profit",
					"label": _("Gross Profit"),
					"icon": "fa fa-bar-chart",
					"onboard": 1,
				},
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
				{
					"type": "page",
					"name": "project-dashboard",
					"label": _("Projects"),
					"icon": "fa fa-bar-chart",
					"onboard": 1,
				},
            ]
        },
        {
            "label": _("Sales"),
            "icon": "octicon octicon-briefcase",
            "items": [
				{
					"type": "page",
					"name": "sales-dashboard",
					"label": _("Sales"),
					"icon": "fa fa-bar-chart",
					"onboard": 1,
				},
				{
					"type": "page",
					"name": "credit-notes",
					"label": _("Credit Notes"),
					"icon": "fa fa-bar-chart",
					"onboard": 1,
				},
            ]
        },
        {
            "label": _("Stores"),
            "icon": "octicon octicon-briefcase",
            "items": [
				{
					"type": "page",
					"name": "stock-dashboard",
					"label": _("Stock"),
					"icon": "fa fa-bar-chart",
					"onboard": 1,
				},
            ]
        },
        {
            "label": _("Support"),
            "icon": "octicon octicon-briefcase",
            "items": [
				{
					"type": "page",
					"name": "support-dashboard",
					"label": _("Support"),
					"icon": "fa fa-bar-chart",
					"onboard": 1,
				},
				{
					"type": "page",
					"name": "technician-time-brea",
					"label": _("Technician Time Breakdown"),
					"icon": "fa fa-bar-chart",
					"onboard": 1,
				},
            ]
        },
    ]