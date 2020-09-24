# noinspection PyStatementEffect
{
    'name': 'University Library Management System',
    'summary': 'Manage your library efficiently.',
    'description':
    """Detailed Feature List Library Card: Librarian can create number of Identity card for Students and Staff. Book 
    Information: Librarian can create and update and manage book lists and related data(Category, Description, 
    Author name,). Book Availability: students can see the availability of books Book Issuance: Librarian can grant 
    new book requests,track due date of issued books(You can set the days to keep the book,you can also set the fine 
    if the preset days exceeds) Return policy:  and returned books. """,
    'author': "Matt O'Bell Ltd, Peter Ajiboye",
    'website': "http://www.mattobell.net",
    'category': 'Extra Tools',
    'version': '13.0.0.1',
    'depends': ['uni_base', 'mail', 'stock'],
    'application': 'True',
    'installable': 'True',
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/book_view.xml',
        'views/member_view.xml',
        'views/product_view.xml',
        'data/sequence.xml',
    ],
}
