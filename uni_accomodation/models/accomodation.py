from odoo import models, fields, api

class saleOrderInherit(models.Model):
    _inherit = 'sale.order'
    name= fields.Char(string='Name')

class StudentAccomodation(models.Model):
    _name= 'student.accomodation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description= 'Accomodation'

    #fields
    matric_no = fields.Char(string='Matric Number', required=True)
    name = fields.Char(string='Name')
    image= fields.Binary(string="Image", related="")
    gender = fields.Selection([
         ("male", "Male"),
         ("fe_male","Female"),
         ], string="Gender", related="")

    #fields for school accomodation
    school_accomodation= fields.Selection([
         ("Madam Tinubu hall", "Madam Tinubu hall"),
         ("King Jaja", "King Jaja"),
         ("Queen Amina Hall", "Queen Amina Hall"),
         ("Princess Adeyemi Hall", "Princess Adeyemi Hall"),
         ("Biobaku Hall", "Biobaku Hall"),
         ],string="School Accomodation")

    @api.model
    def create(self, vals):
             vals ['name'] = self.env['ir.sequence'].next_by_code('student.accomodation.sequence')
             result = super(StudentAccomodation, self).create(vals)
             return result
    


    


  
  

