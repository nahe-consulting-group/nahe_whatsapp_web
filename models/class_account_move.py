from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_sendwsfactura(self):
        settings = self.env['whatsapp.settings'].search([], limit=1)
        if not settings or not settings.invoice_message:
            raise ValidationError('No se ha configurado un mensaje para facturas en WhatsApp.')

        for rec in self:
            message = settings.invoice_message.replace('#CLIENTE', rec.partner_id.display_name)
            message = message.replace('#MONTO', str(round(rec.amount_total, 0)))
            message = message.replace('#FACTURA', rec.name)
            num_cel = rec.partner_id.mobile
            if num_cel:
                num_cel = num_cel.replace('+', '').replace('-', '').replace(' ', '')
                if len(num_cel) == 12 or len(num_cel) == 13:
                    message = message.replace('#NUMERO', num_cel)
                    message = message.replace(' ', '%20')
                else:
                    raise ValidationError(f'Nro de telefono mal formateado: {rec.partner_id.mobile}')
            else:
                raise ValidationError('El cliente no tiene número de celular.')
            return {
                'type': 'ir.actions.act_url',
                'target': 'blank',
                'url': f'https://wa.me/{num_cel}?text={message}'
            }