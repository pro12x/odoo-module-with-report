from odoo import models, fields

class Notary(models.Model):
    _name = 'notary'
    _description = 'Notary'

    name = fields.Char(string='Name', required=True)
    title = fields.Char(string='Title')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    office_id = fields.Many2one('notary.office', string='Notary Office', required=True)
