#-*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hostel Accomodation',
    'version' : '1.1',
    'summary': 'Module for managing hostel accomodation',
    'author': "Matt O'Bell Ltd, Adeyemi Opeyemi",
    'sequence': 3,
    'description': '',
    'category': 'Education',
    'depends' : ['sale', "uni_base",],
    'data': [
        'security/ir.model.access.csv',
        'views/accomodation.xml',
        'views/hostel.xml',
        'views/block.xml',
        'views/room.xml',
        'views/portal.xml',
        "views/floor.xml",
        "data/mail.xml",
        "data/sequence.xml",
        "report/hostel_allocation.xml",
        "report/report.xml",
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}