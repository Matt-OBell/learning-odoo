from odoo import models, fields


class HostelRoom(models.Model):
    _name = 'hostel.room'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Room'
    
    #fields
    name = fields.Char(string="Room No", required=True)
    hostel_id = fields.Many2one("hostel.name", string="Hostel Name")
    room_capacity =fields.Selection([
        ("2", "2 Man Room"),
        ("4", "4 Man Room"),
        ("8", "8 Man room"),
        ], string="Room Capacity")
