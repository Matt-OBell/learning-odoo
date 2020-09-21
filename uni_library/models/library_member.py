from datetime import date
from odoo import models, fields, api


class Member(models.Model):
    _name = 'library.member'
    _description = 'Members'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='Name', required=True)
    email = fields.Char(required=True)
    date_of_membership = fields.Date(
        string='Date of Membership', default=date.today())
    library_id = fields.Char(string='Library ID', readonly=True)
    membership_type = fields.Selection(
        selection=[('staff', 'Staff'), ('student', 'Student')], string="Membership Type")
    total_books_checkout = fields.Integer()
    state = fields.Selection(selection=[('draft', 'New'), ('open', 'Validated'), (
        'confirm', 'Approved')], string='State', readonly=True, default='draft',
        track_visibility='onchange'
    )

    def action_done(self):
       for rec in self:
           member_type = self.env['library.member'].search([])
           print("member type...", member_type)


    def submit(self):
        self.state = 'confirm'

    def pending(self):
        self.state = 'pending'

    def done(self):
        self.state = 'done'

    @api.model
    def create(self, vals):
        print(vals)
        vals['library_id'] = self.env['ir.sequence'].next_by_code(
            'library.member.student')
        res = super(Member, self).create(vals)
        return res

    @api.model
    def create(self, vals):
        print(vals)
        vals['library_id'] = self.env['ir.sequence'].next_by_code(
            'library.member.staff')
        res = super(Member, self).create(vals)
        return res
