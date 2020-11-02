# noinspection PyStatementEffect,SpellCheckingInspection
{
    'name': 'Library',
    'summary': 'Manage your library efficiently.',
    'description': """
    Detailed Feature List: 
    """,
    'author': "Matt O'Bell Ltd, Peter Ajiboye",
    'website': "http://www.mattobell.net",
    'category': 'Extra Tools',
    'version': '13.0.0.1',
    'depends': ['uni_base', 'mail', 'stock'],
    'application': 'True',
    'installable': 'True',
    'data': [
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/product_view.xml',
        'views/res_library_member_view.xml',
        'data/sequence.xml',
    ],
}
