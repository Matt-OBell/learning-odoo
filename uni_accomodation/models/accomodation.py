from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime


class StudentAccomodation(models.Model):
    _name = 'student.accomodation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Accomodation'

    #fields
    matric_no = fields.Many2one(comodel_name='res.student', string='Matric Number', required=True, track_visibility="always")
    name = fields.Char(string='Name', max_length=50)
    image = fields.Binary(string="Image", related="")
    name_seq = fields.Char(string='Hostel Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    faculty = fields.Many2one("uni.faculty", string="Faculty", required=True)
    academic_session = fields.Many2one("uni.session", string="Semester", required=True)
    date = fields.Datetime(
        'Date', required=True, copy=False,
        default=lambda self: fields.Datetime.now())
    hostel_name = fields.Many2one("hostel.name", string="Hostel Name", track_visibility="always")
    hostel_type = fields.Selection([
        ("male", "Male"),
        ("female", "Female"),
        ], string="Gender", required=True, track_visibility="always")
    room_type = fields.Selection([
        ("2", "2 Man Room"),
        ("4", "4 Man Room"),
        ("8", "8 Man room"),
        ("s", "Reserved for Research Scholars"),
        ("p", "Physically Chanllenged"),
        ], string="Room Type")
    bunk = fields.Selection([
        ("Up", "Up Bunk"),
        ("Down", "Down Bunk"),
    ], string="Bunk")
    block_id = fields.Many2one("hostel.block", string="Block")
    room_id = fields.Many2one("hostel.room", string="Room No")
    hostel_portal = fields.Many2one("hostel.portal", string="Portal Details")
    state = fields.Selection(selection=[
        ('draft', 'New'),
        ('submit', 'Open'),
        ('allocated', 'Allocated'),
        ('cancel', 'Cancelled'),
    ], string="State", readonly=True, default="draft")

    @api.model
    def create(self, vals):
        matric_no = vals.get("matric_no")
        academic_session = vals.get("academic_session")    
        domain = [   
            ("matric_no", '=', matric_no),
            ("academic_session", '=', academic_session)
        ]
        accomodations = self.search(domain)
        if accomodations:
            raise ValidationError(_("Accomodation is already allocated to student"))
        vals['name'] = self.env['ir.sequence'].next_by_code('student.accomodation.sequence')
        result = super(StudentAccomodation, self).create(vals)
        return result

    def submit_accomodation(self):
     # Get my email template
        email_template = self.env.ref("uni_accomodation.accomodation_application")
        ctx = self.env.context.copy()
        admin_email = self.matric_no.email
        ctx.update({
            'recipient_email': admin_email,
        })
        email_template.with_context(ctx).send_mail(self.id, force_send=False)
        self.write({"state": "submit"})

    def validate_accomodation(self):
        self.state = 'allocated'

    def approve_accomodation(self):
        self.submit_accomodation()
        self.state = 'allocated'

    def reject_accomodation2(self):
        self.state = 'draft'

    def reject_accomodation(self):
        self.state = 'draft'