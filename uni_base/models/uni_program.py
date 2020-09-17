# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class openuni_faculty(models.Model):
    _name = "uni.faculty"
    _description = "Faculty"
    _order = "name"

    name = fields.Char(string="Name")

    dean_id = fields.Many2one(comodel_name="hr.employee", string="Dean")
    department_ids = fields.One2many(
        "hr.department", "faculty_id", string="Departments"
    )

    # staff_ids = fields.One2many('hr.employee','faculty_id',string='Staffs')
    # student_ids = fields.One2many('res.student','faculty_id',string='Students')


class Program(models.Model):
    _name = "uni.program"
    _description = "Program"

    _order = "name asc"

    name = fields.Char(string="Name", required=True)
    status = fields.Boolean(string="Archive", default=True)
    faculty_id = fields.Many2one(
        comodel_name="uni.faculty", string="Faculty", required=True
    )
    course_ids = fields.Many2many(
        comodel_name="uni.course",
        relation="uni_course_uni_program_rel",
        column2="program_id",
        column1="course_id",
        string="Courses",
    )
    count_courses = fields.Float(string="Count Courses")
    count_elective_courses = fields.Float(string="Electives")
    manager_id = fields.Many2one("hr.employee", string="Manager")
    color = fields.Integer(string="Color Index")
    # document_ids = fields.One2many("ir.attachment", compute="_compute_document_ids", string="Documents")
    # documents_count = fields.Integer(compute="_compute_document_ids", string="Document Count")

    # application_ids = fields.One2many("uni.applicant", "program_id", "Applications")
    # application_count = fields.Integer(compute="_compute_application_count", string="Application Count")
    # new_application_count = fields.Integer(
    #     compute="_compute_new_application_count",
    #     string="New Application",
    #     help="Number of applications that are new in the flow (typically at first step of the flow)",
    # )

    # alias_id = fields.Many2one(
    #     "mail.alias",
    #     "Alias",
    #     ondelete="restrict",
    #     required=True,
    #     help="Email alias for this job position. New emails will automatically create new applicants for this job position.",
    # )
    # color = fields.Integer(string="Color Index")

    # def _compute_document_ids(self):
    #     applicants = self.mapped("application_ids").filtered(lambda self: not self.emp_id)
    #     app_to_job = dict((applicant.id, applicant.program_id.id) for applicant in applicants)
    #     attachments = self.env["ir.attachment"].search(
    #         [
    #             "|",
    #             "&",
    #             ("res_model", "=", "uni.program"),
    #             ("res_id", "in", self.ids),
    #             "&",
    #             ("res_model", "=", "uni.applicant"),
    #             ("res_id", "in", applicants.ids),
    #         ]
    #     )
    #     result = dict.fromkeys(self.ids, self.env["ir.attachment"])
    #     for attachment in attachments:
    #         if attachment.res_model == "uni.applicant":
    #             result[app_to_job[attachment.res_id]] |= attachment
    #         else:
    #             result[attachment.res_id] |= attachment

    #     for job in self:
    #         job.document_ids = result[job.id]
    #         job.documents_count = len(job.document_ids)

    # def _compute_application_count(self):
    #     read_group_result = self.env["uni.applicant"].read_group([("program_id", "in", self.ids)], ["program_id"], ["program_id"])
    #     result = dict((data["program_id"][0], data["program_id_count"]) for data in read_group_result)
    #     for job in self:
    #         job.application_count = result.get(job.id, 0)

    #
