from odoo import models, fields, api, _


class saleOrderInherit(models.Model):
    _inherit = 'sale.order'
    name = fields.Char(string='Name')


class StudentAccomodation(models.Model):
    _name = 'student.accomodation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Accomodation'
    
    #fields
    matric_no = fields.Char(string='Matric Number', required=True )
    name = fields.Char(string='Name')
    image = fields.Binary(string="Image", related="")
    name_seq = fields.Char(string='Hostel Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    faculty = fields.Many2one(
        "uni.faculty", string="Faculty", required=True
    )
    date = fields.Date(string='Date')
    hostel_name = fields.Many2one("hostel.name", string="Hostel Name"
    )
    hostel_type = fields.Selection([
         ("male", "Male"),
         ("female", "Female"),
         ], string="Gender", required=True)
    room_selection = fields.Selection([
          ("2", "2 Man Room"),
          ("4", "4 Man Room"),
          ("8", "8 Man room"),
          ("s", "Reserved for Research Scholars"),
          ("p", "Physically Chanllenged"),
        ], string="Room Selection")
    bunk = fields.Selection([
        ("Up", "Up Bunk"),
        ("Down", "Down Bunk"),
    ], string="Bunk")
    hostel_block = fields.Many2one("hostel.block", string="Block"
    )
    room = fields.Many2one("hostel.room", string="Room No"
    )
    hostel_portal = fields.Many2one("hostel.portal", string="Portal Details"
    )

    @api.model
    def create(self, vals):
             vals['name'] = self.env['ir.sequence'].next_by_code('student.accomodation.sequence')
             result = super(StudentAccomodation, self).create(vals)
             return result

    def submit_allocate(self):
             pass
