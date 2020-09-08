from odoo import models, fields


class HostelRoom(models.Model):
    _name = 'hostel.room'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Room'
    
    #fields
    room_no = fields.Char(string="Room No")
    room_floor = fields.Char(string="Floor")
    