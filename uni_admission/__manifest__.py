# -*- coding: utf-8 -*-
{
    'name': "uni_admission",
    'version': '1.0',
    'category': 'Education',
    'sequence': 3,
    'summary': "Admissions Process""",
    'author': "olajide",
    'application': True,
    'depends': ["base",],
    'description': """
        Management and processing of Admission
    """,

    'data': [
        'security/ir.model.access.csv',
        # 'views/admission_register_view.xml',
        'views/views.xml',
        'menus/uni_menu.xml'
        # 'views/templates.xml',
    ],
}
