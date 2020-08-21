# -*- coding: utf-8 -*-
# from odoo import http


# class UniLibrary(http.Controller):
#     @http.route('/uni_library/uni_library/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/uni_library/uni_library/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('uni_library.listing', {
#             'root': '/uni_library/uni_library',
#             'objects': http.request.env['uni_library.uni_library'].search([]),
#         })

#     @http.route('/uni_library/uni_library/objects/<model("uni_library.uni_library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('uni_library.object', {
#             'object': obj
#         })
