from odoo import fields, models 


class LoanApplication(models.Model):
    _name = 'loan.application' # Technical Name of the model.
    _description = 'Loan Application' # Functional Name of the model.
    
    name = fields.Char(required=True)
    currency_id = fields.Many2one(comodel_name='res.currency', default=lambda self:self.env.company.currency_id.id)
    date_application = fields.Date(string="Applied On", readonly=True)
    date_approval = fields.Date(string="Approved On", readonly=True)
    date_rejection = fields.Date(string="Rejected On", readonly=True)
    date_signed = fields.Datetime(string="Signed On", readonly=True)
    down_payment = fields.Monetary(currency_field="currency_id")
    interest_rate = fields.Float(string="Interest Rate (%)", digits=(5, 4))
    loan_amount = fields.Monetary(currency_field="currency_id")
    loan_term = fields.Integer(string="Loan Term (Months)",required=True, default=36)
    rejection_reason = fields.Text()
    state = fields.Selection(selection=[
        ('draft', 'Draft'), 
        ('sent', 'Sent'), 
        ('review', 'Credit Check'), 
        ('approved', 'Approved'), 
        ('rejected', 'Rejected'), 
        ('signed', 'Signed'), 
        ('cancel', 'Canceled')],
        required=True, default="draft")
    notes = fields.Html()

    # Relational Fields
    partner_id = fields.Many2one(comodel_name='res.partner', string="Customer")
    user_id = fields.Many2one(comodel_name='res.users', string="Salesperson")
    product_id = fields.Many2one(comodel_name='product.product', string="Product")