from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class saleOrderInherit(models.Model):
    _inherit = 'sale.order'
    name = fields.Char(string='Name')

class StudentAccomodation(models.Model):
    _name = 'student.accomodation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Accomodation'  

    #fields
    matric_no = fields.Char(string='Matric Number', max_length=10, required=True, track_visibility="always")
    name = fields.Char(string='Name', max_length=50)
    image = fields.Binary(string="Image", related="")
    name_seq = fields.Char(string='Hostel Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    faculty = fields.Many2one("uni.faculty", string="Faculty", required=True)
    academic_session = fields.Many2one("uni.session", string="Semester", required=True)
    date = fields.Date(string='Date')
    hostel_name = fields.Many2one("hostel.name", string="Hostel Name", track_visibility="always")
    hostel_type = fields.Selection([
        ("male", "Male"),
        ("female", "Female"),
        ], string="Gender", required=True, track_visibility="always")
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
    hostel_block = fields.Many2one("hostel.block", string="Block")
    room = fields.Many2one("hostel.room", string="Room No")
    hostel_portal = fields.Many2one("hostel.portal", string="Portal Details")
    state = fields.Selection(selection=[
        ('draft', 'New'),
        ('submit', 'Open'),
        ('validate', 'Allocated'),
        ('cancel', 'Cancelled'),
    ], string="State", readonly=True, default="draft")



    def create(self, vals):
        matric_no = vals.get("matric_no")
        academic_session = vals.get("academic_session")
    
        domain = [   
            ("matric_no",'=', matric_no),
            ("academic_session", '=', academic_session)
        ]
        accomodations = self.search(domain)
    
        if accomodations:
            raise ValidationError(_("Accomodation is already allocated to student"))
        vals['name'] = self.env['ir.sequence'].next_by_code('student.accomodation.sequence')
        result = super(StudentAccomodation, self).create(vals)
        return result

    def submit_accomodation(self):
        self.write({"state": "submit"})

    def validate_accomodation(self):
        self.state = 'validate'

    def approve_accomodation(self):
        self.state = 'approve'

    def reject_accomodation2(self):
        self.state = 'draft'

    def reject_accomodation(self):
        self.state = 'draft'




