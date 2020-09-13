from odoo import models, fields


class HostelRoom(models.Model):
    _name = 'hostel.room'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Room'
    
    #fields
    name = fields.Char(string="Room No", required=True)
    room_floor = fields.Char(string="Floor", required=True)
    hostel_id = fields.Many2one("hostel.name", string="Hostel Name")

