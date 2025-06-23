from odoo import models, fields, api
from odoo.exceptions import UserError

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def action_post(self):
        res = super().action_post()

        for payment in self:
            if payment.journal_id.type != 'bank':
                continue  # hanya untuk journal tipe bank

            # Cek apakah payment method adalah Giro
            if payment.payment_method_line_id and payment.payment_method_line_id.name == 'Giro':
                continue  # skip jika metode pembayaran adalah Giro

            # Buat baris bank statement
            self.env['account.bank.statement.line'].create({
                'payment_ref': payment.ref or payment.name,
                'partner_id': payment.partner_id.id,
                'amount': payment.amount if payment.payment_type in ['inbound', 'transfer'] else -payment.amount,
                'date': payment.date,
                'journal_id': payment.journal_id.id,
            })

        return res
