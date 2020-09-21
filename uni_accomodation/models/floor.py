from odoo import models, fields, _


class HostelFloor(models.Model):
    _name = 'hostel.floor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Floor'

    #fields
    name = fields.Char(string="Floor")
    room_ids = fields.One2many("hostel.room", "room_floor", string="Room")


    def action_create_room(self):
        pass