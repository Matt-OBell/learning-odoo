from odoo import models, fields


class Category(models.Model):
    _name = 'category.library_book'
    _description = 'Category'
    name = fields.Char(string='Category')


class Book(models.Model):
    _name = 'library.book'
    _description = 'Books'
    name = fields.Char(string='Title', required=True)
    image = fields.Binary()
    author_ids = fields.Many2many('res.partner', string='Authors')
    isbn = fields.Char(string='ISBN')
    published_date = fields.Date()
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    active = fields.Boolean('Active?', default=True)
    #category = fields.Char()
    category = fields.Many2many('category.library_book')
