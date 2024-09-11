from odoo import models, fields, api
from odoo.exceptions import ValidationError


class WhatsappSettings(models.Model):
    _name = "whatsapp.settings"
    _description = "WhatsApp Settings"
    _rec_name = "name"

    name = fields.Char(default="Configuración de WhatsApp", readonly=True)
    sale_message = fields.Text(string="Mensaje de Venta")
    invoice_message = fields.Text(string="Mensaje de Factura")
    purchase_message = fields.Text(string="Mensaje de Compra")

    @api.model
    def create(self, vals):
        if self.search([]):
            raise ValidationError(
                "Solo se puede crear un registro de configuración de WhatsApp."
            )
        return super(WhatsappSettings, self).create(vals)
