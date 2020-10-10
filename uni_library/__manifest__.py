# noinspection PyStatementEffect,SpellCheckingInspection
{
    'name': 'Library',
    'summary': 'Manage your library efficiently.',
    'description': """Detailed Feature List
    Library Card: The system can create number of Identity card for Students and Staff. [done]
    Book Information: The system can create and update and manage book lists and related data [done]
    Book checkout: Decreases the number of book items when a checkout has been made
    Book Issuance: The system can grant new book requests,track due date of issued books
    (You can set the days to keep the book,you can also set the fine if the preset days exceeds) 
    Return policy:
    Book Lending:
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
