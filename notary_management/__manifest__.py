{
    'name': 'Notary Management',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Module for managing notary offices',
    'description': """
        This module helps to manage notary offices including notaries, 
        current accounts, and provides a printable report for Notary Offices.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/notary_views.xml',
        'views/notary_office_views.xml',
        'reports/notary_office_template.xml',
        'views/current_account_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'odoo_notary_management/static/description/icon.png',
        ],
    },
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
}
