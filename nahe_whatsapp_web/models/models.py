# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class nahe_whatsapp_web_so(models.Model):
     _inherit = 'sale.order'
     _description = 'nahe_whatsapp_web.nahe_whatsapp_web'
     
     def action_sendwslisto(self, default=None):
          WS_MESSAGE = self.env['ir.config_parameter'].get_param('nahe_whatsapp_web.MENSAJESO','')
          #https://wa.me/#NUMERO?text=Buen%20dia,%20#CLIENTE%20su%20pedido%20#ORDEN%20esta%20listo%20para%20retirar.%20Total%20#MONTO
          for rec in self:
               message = WS_MESSAGE.replace('#CLIENTE',rec.partner_id.display_name)
               message = message.replace('#MONTO',str(round(rec.amount_total,0)))
               message = message.replace('#ORDEN',rec.name)
               num_cel = rec.partner_id.mobile
               if num_cel:
                    num_cel = num_cel.replace('+','')
                    num_cel = num_cel.replace('-','')
                    num_cel = num_cel.replace(' ','')
                    if len(num_cel) == 12 or len(num_cel) == 13:
                         message = message.replace('#NUMERO',num_cel)
                         #LIMPIAMOS LOS ESPACIOS POR LAS DUDAS
                         message = message.replace(' ','%20')
                    else:
                         raise ValidationError('Nro de telefono mal formateado whatsapp necesita codigo de pais en el numero %s'%(rec.mobile))
               else:
                    raise ValidationError('El cliente no tiene numero de celular agendado')
          return {
                   'type': 'ir.actions.act_url',
                   'target': 'blank',
                   'url': message
            }
class nahe_whatsapp_web_invoice(models.Model):
     _inherit = 'account.move'
     _description = 'nahe_whatsapp_web.nahe_whatsapp_web_account_move'
     def action_sendwsfactura(self, default=None):
          WS_MESSAGE = self.env['ir.config_parameter'].get_param('nahe_whatsapp_web.MENSAJEINVOICE','')
          #https://wa.me/send?#NUMERO?text=Buen%20dia,%20#CLIENTE%20su%20factura%20#FACTURA%20esta%20disponible%20para%20abonar.%20Total%20#MONTO
          for rec in self:
               message = WS_MESSAGE.replace('#CLIENTE',rec.partner_id.display_name)
               message = message.replace('#MONTO',str(round(rec.amount_total,0)))
               message = message.replace('#FACTURA',rec.name)
               num_cel = rec.partner_id.mobile
               if num_cel:
                    num_cel = num_cel.replace('+','')
                    num_cel = num_cel.replace('-','')
                    num_cel = num_cel.replace(' ','')
                    if len(num_cel) == 12 or len(num_cel) == 13:
                         message = message.replace('#NUMERO',num_cel)
                         #LIMPIAMOS LOS ESPACIOS POR LAS DUDAS
                         message = message.replace(' ','%20')
                    else:
                         raise ValidationError('Nro de telefono mal formateado whatsapp necesita codigo de pais en el numero %s'%(rec.partner_id.mobile))
               else:
                    raise ValidationError('El cliente no tiene numero de celular agendado')
          return {
                   'type': 'ir.actions.act_url',
                   'target': 'blank',
                   'url': message
            }
class nahe_whatsapp_web_purchase(models.Model):
     _inherit = 'purchase.order'
     _description = 'nahe_whatsapp_web.nahe_whatsapp_web_purchase_order'
     def action_sendwscompra(self, default=None):
          WS_MESSAGE = self.env['ir.config_parameter'].get_param('nahe_whatsapp_web.MENSAJEPURCHASE','')
          #https://wa.me/send?#NUMERO?text=Buen%20dia,%20#PROVEEDOR%20nos%20comunicamos%20por%20este%pedido%20que%20adjuntamos
          for rec in self:
               message = WS_MESSAGE.replace('#PROVEEDOR',rec.partner_id.display_name)
               num_cel = rec.partner_id.mobile
               if num_cel:
                    num_cel = num_cel.replace('+','')
                    num_cel = num_cel.replace('-','')
                    num_cel = num_cel.replace(' ','')
                    if len(num_cel) == 12 or len(num_cel) == 13:
                         message = message.replace('#NUMERO',num_cel)
                         #LIMPIAMOS LOS ESPACIOS POR LAS DUDAS
                         message = message.replace(' ','%20')
                    else:
                         raise ValidationError('Nro de telefono mal formateado whatsapp necesita codigo de pais en el numero %s'%(rec.partner_id.mobile))
               else:
                    raise ValidationError('El cliente no tiene numero de celular agendado')
          return {
                   'type': 'ir.actions.act_url',
                   'target': 'blank',
                   'url': message
            }
