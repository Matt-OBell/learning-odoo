# -*- coding: utf-8 -*-

from odoo import models, fields, api


class uni_library(models.Model):
    _name = 'uni_library.uni_library'
    _description = 'Library Management System'
    name = fields.Char('Title', required=True)
    isbn = fields.Char(string='ISBN')
    active = fields.Boolean('Active?', default=True)
    date_published = fields.Date()
    # image = fields.Binary()
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    author_ids = fields.Many2many('res.partner', string='Authors')

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
