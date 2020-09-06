{
    'name': 'University Library Management System',
    'summary': 'A Module for managing library.',
    'description': 'Library Management System',
    'author': "Matt O'Bell Ltd, Peter Ajiboye",
    'website': "http://www.mattobell.net",
    'category': 'Extra Tools',
    'version': '13.0.0.1',
    'depends': ['base', 'uni_base'],
    'application': 'True',
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
    ],
}
