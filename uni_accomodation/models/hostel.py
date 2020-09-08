from odoo import models, fields, _


class HostelName(models.Model):
    _name = 'hostel.name'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hostel'
    
    #fields
    hostel_name = fields.Char(string="Hostel Name")
    hostel_no = fields.Integer(string='Hostel No')