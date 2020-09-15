# -*- coding: utf-8 -*-

from odoo import api, fields, models

SEMESTER_TYPE = [
    ("rain", "Rain Semester"),
    ("harmattan", "Harmattan Semester"),
]


class Level(models.Model):
    """openuniversity session class"""

    _name = "uni.level"
    _description = "Level"
    name = fields.Char(string="Name", required=True)

    sequence = fields.Integer(string="Sequence", required=True)
    course_ids = fields.One2many("uni.course", "level_id", string="Courses")
    student_ids = fields.One2many("res.student", "level_id", string="Students")


class Session(models.Model):
    """openuniversity session class"""

    _name = "uni.session"
    _description = "Session"
    _inherit = ["mail.thread"]

    name = fields.Char(string="Name", required=True)
    start_date = fields.Date(string="Date Start", required=True)
    end_date = fields.Date(string="Date End", required=True)
    semester_ids = fields.One2many("uni.semester", "session_id", string="Semesters")


class Semester(models.Model):
    """Open university Semester"""

    _name = "uni.semester"
    _description = "Semester"

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    semester_type = fields.Selection(
        selection=SEMESTER_TYPE, required=True, string="Type"
    )
    session_id = fields.Many2one(
        comodel_name="uni.session", string="Session", required=True
    )
    start_date = fields.Date(string="Semester Start", required=True)
    end_date = fields.Date(string="Semester End", required=True)
    course_registration = fields.Selection(
        selection=[("open", "Open"), ("closed", "Closed")], string="Registration"
    )
    allow_registration = fields.Boolean(string="Late Registration")

    registration_start_date = fields.Datetime(
        string="Registration Start", required=True
    )
    registration_end_date = fields.Datetime(string="Registration End", required=True)

    clearance_start_date = fields.Datetime(string="Clearance Start")
    clearance_end_date = fields.Datetime(string="Clearance End")
