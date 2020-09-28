from odoo import models, fields, _


class HostelName(models.Model):
    _name = 'hostel.name'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hostel'
    
    #fields
    name = fields.Char(string="Hostel Name",required=True)
    room = fields.One2many("hostel.room", "hostel_id", string="Room")
    block = fields.One2many("hostel.block", "hostel_id", string="Block")
    floor = fields.One2many("hostel.floor", "hostel_id", string="Floor")
