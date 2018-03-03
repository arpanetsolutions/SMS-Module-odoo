# -*- coding: utf-8 -*-
{
    "name": "Arpanet Sms Integration",
    "version": "1.0",
    "description": """
    Module Which Provides Sms Integration With Dynasoft.
    """,
    "author": "Arpanet Solution",
    "website": "www.arpanetsolutions.com",
    'category': 'sale',
    "depends": ['base', 'crm', 'contacts'],
    "data": [
            'security/ir.model.access.csv',
            'views/schedular_view.xml',
            'views/sms_config_view.xml',
            'views/sms_sms_view.xml',
            'views/sms_scheduled_view.xml',
            'views/crm_lead_view.xml'
        ],
    'installable': True,
    'auto_install': False
}
