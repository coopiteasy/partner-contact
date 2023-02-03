from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    subject_to_vat = fields.Boolean(string="Subject to VAT")
