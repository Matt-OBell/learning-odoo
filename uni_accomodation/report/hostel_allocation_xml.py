from odoo import models


class HostelAllocationXLS(models.AbstractModel):
    _name = "report.uni_accomodation.report_hostel_xls"
    _inherit = "report.report_xlsx.abstract"
      

    def generate_xlsx_report(self, workbook, data, lines):
        print("lines", "lines", "data")
        # format1 = workbook.add_format({'font_size':14, "align": "vcentre", "bold":True})
        # format2 = workbook.add_format({'font_size':10, "align": "vcentre",})
        # sheet = workbook.add_worksheet("Hostel Name")
        # sheet.write(2, 2, "Matric No", format1)
        # sheet.write(2, 3, lines.matric_no, format2)
        # sheet.write(3, 2, "Hostel Name", format1)
        # sheet.write(3, 3, lines.hostel_name, format2)