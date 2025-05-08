# -*- coding: utf-8 -*-
# from odoo import http


# class DpmReconciliation(http.Controller):
#     @http.route('/dpm_reconciliation/dpm_reconciliation', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dpm_reconciliation/dpm_reconciliation/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dpm_reconciliation.listing', {
#             'root': '/dpm_reconciliation/dpm_reconciliation',
#             'objects': http.request.env['dpm_reconciliation.dpm_reconciliation'].search([]),
#         })

#     @http.route('/dpm_reconciliation/dpm_reconciliation/objects/<model("dpm_reconciliation.dpm_reconciliation"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dpm_reconciliation.object', {
#             'object': obj
#         })

