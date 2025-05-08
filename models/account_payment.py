from odoo import models, fields, api
from odoo.exceptions import UserError


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def action_post(self):
        res = super().action_post()

        for payment in self:
            if payment.journal_id.type != 'bank':
                continue  # hanya untuk journal tipe bank

            bank_journal = payment.journal_id

            # Cari atau buat bank statement yang masih draft
            statement = self.env['account.bank.statement'].search([
                ('journal_id', '=', bank_journal.id),
                ('date', '=', payment.date),
            ], limit=1)

            if not statement:
                statement = self.env['account.bank.statement'].create({
                    'journal_id': bank_journal.id,
                    'date': payment.date,
                    'name': f"{payment.name}",
                })

            # Buat baris bank statement
            self.env['account.bank.statement.line'].create({
                'statement_id': statement.id,
                'payment_ref': payment.ref or payment.name,
                'partner_id': payment.partner_id.id,
                'amount': payment.amount if payment.payment_type in ['inbound', 'transfer'] else -payment.amount,
                'date': payment.date,
                'journal_id': bank_journal.id,
            })

        return res
