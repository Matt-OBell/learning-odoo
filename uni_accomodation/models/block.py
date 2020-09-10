from odoo import models, fields, _


class HostelBlock(models.Model):
    _name = 'hostel.block'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Block'
    
    #fields
    name = fields.Char(string="Block No", required=True)
    block_id = fields.Char(string="Block ID")
    hostel_id = fields.Many2one('hostel.name', string="Hostel Name")
    