from odoo import api, fields, models
#from odoo.exceptions import Warning


class ProductTemplate(models.Model):
    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check
    _inherit = 'product.template'
    _description = 'Category'
    is_a_book = fields.Boolean(string="Is A Book?")
    author_ids = fields.Many2many('res.partner', string='Authors')
    isbn = fields.Char(string='ISBN')
    published_date = fields.Date(string='Published Date')
    publisher_id = fields.Many2one('res.partner', string='Publisher', index=True)
    is_available = fields.Boolean(string='Is Available?')
    active = fields.Boolean('Active?', default=True)

    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check