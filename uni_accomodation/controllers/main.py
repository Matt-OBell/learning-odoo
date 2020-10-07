from odoo import http
from odoo.http import request
# from odoo.addons.website_sale.controllers.main import websiteSale


class AccomodationController(http.Controller):
    @http.route('/uni_accomodation/accomodation', auth='user', type='http', website=True)
    def accomodation_banner(self):
        return request.render("uni_accomodation.accomodation")
        