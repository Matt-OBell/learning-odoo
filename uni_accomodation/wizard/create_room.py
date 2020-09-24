from odoo import models, fields, api


class CreateRoom(models.TransientModel):
    _name = 'create.room'
    _description = "Wizard: Room Creating Portal"


    room_id = fields.Many2one('hostel.floor', string="Room No", required=True)