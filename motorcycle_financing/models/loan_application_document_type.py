from odoo import api, fields, models


class LoanApplicationDocumentType(models.Model):
    _name = "loan.application.document.type"
    _description = "Loan Application Document Type"

    name = fields.Char()
    active = fields.Boolean(default=True)