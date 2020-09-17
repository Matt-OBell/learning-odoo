from odoo import models, fields, _


class HostelPortal(models.Model):
    _name = 'hostel.portal'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Portal'
    
    #fields
    portal_id = fields.Many2one("res.user", string="Staff ID"
    )
    name = fields.Char(String="Portal Name")
    portal_gender = fields.Selection([
         ("male", "Male"),
         ("female", "Female"),
         ], string="Gender", required=True)