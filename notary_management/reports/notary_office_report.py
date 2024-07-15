from odoo import models, api

class NotaryOfficeReport(models.AbstractModel):
    _name = 'report.odoo_notary_management.notary_office_report_template'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['notary.office'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'notary.office',
            'docs': docs,
        }
