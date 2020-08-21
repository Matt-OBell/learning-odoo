# -*- coding: utf-8 -*-
{
    'name': "University Library",

    'summary': 'A Library Management System for &UNIVERSITY_NAME',

    'description': 'University Library Management System',

    'author': "Matt O'Bell Ltd, Peter Ajiboye",
    # 'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '13.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'uni_base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
