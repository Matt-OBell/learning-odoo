{
    'name': 'University Library Management System',
    'summary': 'Manage your library efficiently.',
    'description':
    """Detailed Feature List
    Card Details: Librarian can create number of Identity card for Students.
    Book Information: Librarian can create and update and manage book lists and related data.
    Book Availability: 
    Book Issuance: Librarian can grant new book requests,track issued books
    Return policy:  and returned books.
    """,
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
