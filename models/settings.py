from odoo import models, fields, api
from odoo.exceptions import ValidationError

class WhatsAppSettings(models.Model):
    _name = 'whatsapp.settings'
    _description = 'Configuración de mensajes para WhatsApp'

    name = fields.Char(string="Nombre", required=True)
    sale_message = fields.Text(string="Mensaje para Pedido")
    invoice_message = fields.Text(string="Mensaje para Factura")
    purchase_message = fields.Text(string="Mensaje para Compra")
