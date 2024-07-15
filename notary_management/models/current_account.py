from odoo import models, fields

class CurrentAccount(models.Model):
    _name = 'current.account'
    _description = 'Current Account'

    number = fields.Char(string='Account Number', required=True)
    office_id = fields.Many2one('notary.office', string='Notary Office', required=True)
    balance = fields.Float(string='Balance')
    creation_date = fields.Date(string='Creation Date')
