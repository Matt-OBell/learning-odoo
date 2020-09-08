from odoo import models, fields, _


class HostelBlock(models.Model):
    _name = 'hostel.block'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Block'
    
    #fields
    block_no = fields.Char(string="Block No")
    block_id = fields.Char(string="Block ID")
    