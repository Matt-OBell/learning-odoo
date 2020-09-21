from odoo import models, fields, _


class HostelFloor(models.Model):
    _name = 'hostel.floor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Floor'

    #fields
    name = fields.Char(string="Floor")
    hostel_id = fields.Many2one('hostel.name', string="Floor")



    def action_create_room(self):
        self.env["hostel.room"].create({"name":"", "hostel_id":"", "room_capacity":""})
