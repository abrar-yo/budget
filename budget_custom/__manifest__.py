# -*- coding: utf-8 -*-
{
    'name': 'Custom Budget',
    'summary': 'Accounting Budget Modifications',
    'description': """Budget Modifications """,
    'author': "Canyons Business Solutions",
    'website': "https://canyons-sd.com/",
    'category': 'Accounting',
    'version': '0.1',
    'sequence': -100,
    'license': "LGPL-3",

    # any module necessary for this one to work correctly
    'depends': ['base','account', 'account_budget'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/budget_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
