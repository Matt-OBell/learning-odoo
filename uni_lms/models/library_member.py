from odoo import models, fields


class Member(models.Model):
    _name = 'library.member'
    _description = 'Members'
    name = fields.Char(string='Name', required=True)
    date_of_membership = fields.Date(string='Date of Membership')
    total_books_checkout = fields.Integer()
