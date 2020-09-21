# -*- coding: utf-8 -*-

from odoo import api, fields, models

DEPARTMENT_TYPE = [("aca", "Academy"), ("non", "Non Academy")]
DELIVERY_MODE = [
    ("f2f", "Face-to-Face (F2F)"),
    ("hcd", "Hybrid Course Delivery"),
    ("focd", "Fully Online Course Delivery"),
]


class Course(models.Model):
    _name = "uni.course"
    _description = "Course"

    is_elective = fields.Boolean(string="Elective")
    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Course Title", required=True)
    unit = fields.Integer(string="Course Unit", required=True)
    level_id = fields.Many2one("uni.level", string="Level", required=True)
    program_ids = fields.Many2many(
        comodel_name="uni.program",
        relation="uni_course_uni_program_rel",
        column1="program_id",
        column2="course_id",
        string="Program(s)",
    )
    code = fields.Char(string="Course Code", size=8, required=True)
    department_id = fields.Many2one("hr.department", string="Department", required=True)
    delivery_mode = fields.Selection(
        selection=DELIVERY_MODE,
        string="Delivery Mode",
        default="f2f",
        help="""
        * A Face-to-Face (F2F) course is delivered in the traditional classroom setting. 
        This means that scheduled normative hours take place in the physical classroom.

        * A hybrid (or blended) course combines in-class instruction and activities with flexible, 
        guided online learning in a virtual environment.

        * A fully online course is delivered in the virtual classroom. 
        This means that scheduled normative hours take place outside of a physical classroom

        """,
    )

    # course_schedule_ids = fields.Many2many('openuni.course_schedule',string='Course Schedules')
    # minimum_grade = fields.Float('Minimum Grade')
    # general_course_ids = fields.One2many('openuni.general_course','course_id','General Courses')
    # staff_ids = fields.Many2many('hr.employee',string='Staffs')
    # faculty_id = fields.Many2one('openuni.faculty',string='Faculty')
    # # course_reg_no = fields.Function(_get_course_reg, string='Course Reg. No.', type="char", size=64, store=True, method=True)
    # prerequisite_ids = fields.One2many('openuni.prerequisite_course','course_id',string='Prerequisite Courses')
    # prerequisite_course_ids = fields.Many2many('openuni.prerequisite_course',string='Prerequisites',)
    # registered_course_core_ids = fields.One2many('openuni.registered_course_core','course_id',string='Registered Core Courses')
    # grade_book_ids = fields.One2many('openuni.grade_book','course_id',string='Grade Books')
