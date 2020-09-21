# -*- coding: utf-8 -*-

{
    "name": "University Base",
    "category": "Education",
    "summary": "University Base Module",
    "description": """ University base module""",
    "depends": ["base", "mail", "hr"],
    "data": [
        "security/ir.model.access.csv",
        #
        "data/uni_faculty.xml",
        "data/uni_program.xml",
        #
        "views/management.xml",
        "views/session.xml",
        "views/student_view.xml",
        "views/student_actions.xml",
        "views/hr_department.xml",
    ],
    "application": True,
}
