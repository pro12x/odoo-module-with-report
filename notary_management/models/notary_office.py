from odoo import models, fields, api

class NotaryOffice(models.Model):
    _name = 'notary.office'
    _description = 'Notary Office'

    name = fields.Char(string='Office Name', required=True)
    ninea = fields.Char(string='NINEA', required=True)
    address = fields.Char(string='Address')
    zone = fields.Char(string='Zone')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    notary_ids = fields.One2many('notary', 'office_id', string='Notaries')
    account_ids = fields.One2many('current.account', 'office_id', string='Current Accounts')
