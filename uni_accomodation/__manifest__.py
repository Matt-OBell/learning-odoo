#-*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hostel Accomodation',
    'version' : '1.1',
    'summary': 'Module for managing hostel accomodation',
    'sequence': 3,
    'description': '',
    'category': 'Education',
    'depends' : ['mail','sale',],
    'data': [
       'security/ir.model.access.csv',
        'views/accomodation.xml' ,
    ],
    'demo': [''],
    'installable': True,
    'application': True,
    'auto_install': False,
}
