from odoo import models, fields


class Management(models.Model):
    _name = 'library.management'
    _description = 'Management'
    name = fields.Char()
