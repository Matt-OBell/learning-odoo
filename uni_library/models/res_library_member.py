from datetime import date
from odoo import api, models, fields


# noinspection PyTypeChecker
class LibraryMember(models.Model):
    _name = 'res.library.member'
    _description = 'Library Member'
    borrowers_number = fields.Integer(string="Borrower's Number")
    course = fields.Char(string='Course')
    department = fields.Char(string='Department')
    date_of_membership = fields.Date(string='Date of Membership', default=date.today(), readonly=True)
    email = fields.Char(string='Email')
    faculty = fields.Many2one('res.partner', string='Faculty')
    level = fields.Integer(string='Level')
    library_id = fields.Char(string='Library ID', readonly=True)
    home_address = fields.Char(string='Home Address')
    hall = fields.Many2one('res.partner', string='Hall')
    matriculation_number = field.Integer(string = 'Matriculation Number')
    phone_number = fields.Integer(string='Phone Number')
    passport = fields.Binary('Cover')
    room_number = fields.Integer(string='Room Number')
    session = fields.Integer(string='Session')
    student_id = fields.Many2one(
        'res.student', delegate=True, ondelete='cascade', required="False")
    total_books_checkout = fields.Integer(string='Total Books Checkout')
    # signature = fields.''

    # def action_done(self):
    #     for rec in self:
    #         membership_type = self.env['res.library.member'].search([])
    #         print("member type...", membership_type)
    #
    #
    # @api.model
    # def create(self, vals):               
    #     print(vals)
    #     vals['library_id'] = self.env['ir.sequence'].next_by_code(
    #         'res.library.member.student')
    #     res = super(LibraryMember, self).create(vals)
    #     return res
    # @api.model
    # def create(self, vals):
    #     print(vals)
    #     vals['library_id'] = self.env['ir.sequence'].next_by_code(
    #         'res.library.member.staff')
    #     res = super(LibraryMember, self).create(vals)
    #     return res
