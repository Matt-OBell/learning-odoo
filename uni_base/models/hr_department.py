# -*- coding: utf-8 -*-

from odoo import api, fields, models

DEPARTMENT_TYPE = [("aca", "Academy"), ("non", "Non Academy")]


class HrDepartment(models.Model):
    _inherit = "hr.department"

    manager_id = fields.Many2one(comodel_name="hr.employee", string="H.O.D")
    department_type = fields.Selection(selection=DEPARTMENT_TYPE, string="Type")
    student_ids = fields.One2many("res.student", "department_id", string="Students")
    faculty_id = fields.Many2one(comodel_name="uni.faculty", string="Faculty")
