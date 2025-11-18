from odoo import fields, models 


class CoModelName(models.Model):
    _name = 'comodel.name' # Technical Name of the model.
    _description = 'Comodel Name' # Functional Name of the model.

    name = fields.Char(required=True) #

    field_2many = fields.One2many(comodel_name='model.name', inverse_name="field_2one")