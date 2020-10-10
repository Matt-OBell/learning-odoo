from datetime import date
from odoo import api, models, fields


# noinspection PyTypeChecker
class LibraryMember(models.Model):
    _name = 'res.library.member'
    _description = 'Library Member'
    student_id = fields.Many2one(
        'res.student',
        delegate=True,
        ondelete='cascade',
        required="False")
    library_id = fields.Char(string='Library ID', readonly=True)
    date_of_membership = fields.Date(string='Date of Membership', default=date.today(), readonly=True)
    total_books_checkout = fields.Integer()

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
