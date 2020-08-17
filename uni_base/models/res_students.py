from odoo import models, fields, api


class Student(models.Model):
    _name = "res.student"

    _inherits = {"res.partner": "partner_id"}
    _description = "Students"

    partner_id = fields.Many2one(
        comodel_name="res.partner", string="Related Partner", required=True, ondelete="cascade",
    )
    department_id = fields.Many2one(
        comodel_name="hr.department", string="Department", required=True, ondelete="cascade",
    )
    level_id = fields.Many2one(comodel_name="uni.level", string="Level", required=True)


#     def send_mail(self, cr, uid, ids,module_name,template_id,context=None):
#         email_template_obj = self.pool.get('email.template')
#         # Traces the ID in the Data xml file to get the ID that was stored in the database
#         template_id = self.pool.get('ir.model.data').get_object_reference(cr, uid,module_name,template_id)[1]
#         if template_id:
#               values = email_template_obj.generate_email(cr, uid, template_id, ids, context=context)
#               record_id = values['res_id'][0]
#               ans=email_template_obj.send_mail(cr, uid, template_id,record_id,True,context=context)

#         return True

#     image = fields.Binary(string='Image')
#     hold_type_ids = fields.Many2many('openuni.hold_type',string='Hold Types')
#     status_ids = fields.Many2many('openuni.status',string='Status')
#     first_name = fields.Char(string='First Name')
#     middle_name = fields.Char(string='Middle Name')
#     last_name = fields.Char(string='Last Name')
#     admission_no = fields.Char(string='Admission No', readonly=True)
#     department_id = fields.Many2one('openuni.department',string='Department',required=True)
#     level_id = fields.Many2one('openuni.level',string='Level',required=True)
#     jamb_reg_no = fields.Char(string='Jamb Reg. Number',readonly=True)
#     matric_no = fields.Char(string='Matric. Number',readonly=True)
#     sex = fields.Selection([('m','male'),('f','female')],string='Sex')
#     country_id = fields.Many2one('res.country',string='Country')
#     state_id = fields.Many2one('res.country.state',string='State of Origin')
#     lga_id = fields.Many2one('openuni.lga',string='LGA')
#     dob = fields.Date(string='DOB')
#     phone = fields.Char(string='Phone No.')
#         'faculty_id': fields.Many2one('openuni.faculty',string='Faculty'),
#     partner_id = fields.Many2one('res.partner',string='Related Partner')
#         'is_matriculated': fields.Boolean(string='Matriculated'),
#     course_schedule_ids = fields.Many2many('openuni.course_schedule',string='Course Schedules')
#         'guardian_ids1': fields.One2many('openuni.guardian','student_id',string='Parent/Guardian'),
#     application_high_school_ids1 = fields.One2many('openuni.application_high_school','student_id',string='School Names')
#         'examination_result_ids1': fields.One2many('openuni.examination_result','student_id',string='Examination Results'),
#     student_grade_ids = fields.One2many('openuni.student_grade','student_id',string='Students')
#     registered_course_core_ids = fields.One2many('openuni.registered_course_core','student_id',string='Registered Core Courses')
#     registered_course_general_ids = fields.One2many('openuni.registered_course_general','student_id',string='Registered General/Eds Courses')
#     registered_course_elective_ids = fields.One2many('openuni.registered_course_elective','student_id',string='Registered Elective Courses')


#     _defaults = {
#         'country_id': 164,
#         }

#     _sql_constraints = [
#         ('jamb_reg_no_uniq', 'unique(jamb_reg_no)', 'No two Students can have thesame Jamb Reg. No!'),
#         ('admission_no_uniq', 'unique(admission_no)', 'No two Students can have thesame Admission No!'),
#         ('matric_no_uniq', 'unique(matric_no)', 'No two Students can have thesame Matric No!'),
#     ]

#     def on_change_fieldname(self,cr,uid,ids,field_name,context=None):
# #         obj = self.pool.get('res.country.state')
# #         ids=obj.search(cr,uid,[('country_id','=',country_id)])
# #         obj_browse=obj.browse(cr,uid,ids)
#         res = {}
#         res['value']={field_name:0}
# #         if obj_browse:
# #             res['domain']= {'state':[('country_id','=',country_id)]}
#         return res


#     def action_matriculate(self, cr, uid, ids, context=None):
#         for record in self.browse(cr,uid,ids,context=context) :
#             data =   [(6, 0, [self.pool.get('ir.model.data').get_object_reference(cr,uid,'ng_openuni','openuni_default_status3')[1]])]
#             matric_no = self.pool.get('ir.sequence').get(cr, uid, 'matric_id_code') or '',
#             matric_no = str(matric_no)[3:-3]
#             self.write(cr, uid, ids, {'status_ids':data,'is_matriculated':True, 'matric_no':matric_no}, context=context)

#     def create(self, cr, uid, vals, context=None):
#          # Create the customer data

#         if vals.get('country_id',False):

#             cust_model = self.pool.get('res.partner')
#             cust_data = {
#                         'name' : vals['first_name'] + ' ' + vals['last_name'],
#                          #'street' : applicant_obj.street1,
#                          #'city' : applicant_obj.city,
#                          'image':vals['image'],
#                          #'user_id':user_id,
#                          'function': 'Student',
#                          'country_id': vals['country_id'],
#                          'type':'contact',
#                          #'email': applicant_obj.email,
#                          #'street2':applicant_obj.street2,
#                          'phone': vals['phone'],
#                          'customer':True,
#                          #'image_medium':applicant_obj.applicant_image,
#                          #'mobile': applicant_obj.telephone2,
#                          #'image_small':applicant_obj.applicant_image,
#                          'display_name':vals['first_name'] + ' ' + vals['last_name'],
#                          #'ref':'i ma the ref',
#                          }

#             cust_id = cust_model.create(cr,uid,cust_data,context)

#             if cust_data:
#                 ans=self.send_mail( cr, uid, ids, 'ng_openuni', 'email_templ_openuni_admission_admit',context)


#         return super(openuni_student, self).create(cr, uid, vals, context)
