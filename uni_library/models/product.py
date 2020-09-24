from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description ='Category'

    is_a_book = fields.Boolean(string="Is A Book?")