from odoo import models, fields


class Book(models.Model):
    _name = 'library.book'
    _description = 'Books'
    name = fields.Char(string='Title', required=True) 
    isbn = fields.Char(string='ISBN')
    active = fields.Boolean('Active?', default=True)
    published_date = fields.Date()
    image = fields.Binary()
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    author_ids = fields.Many2many('res.partner', string='Authors')
