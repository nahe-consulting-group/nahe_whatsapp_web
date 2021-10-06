# -*- coding: utf-8 -*-
# from odoo import http


# class NaheWhatsappWeb(http.Controller):
#     @http.route('/nahe_whatsapp_web/nahe_whatsapp_web/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nahe_whatsapp_web/nahe_whatsapp_web/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nahe_whatsapp_web.listing', {
#             'root': '/nahe_whatsapp_web/nahe_whatsapp_web',
#             'objects': http.request.env['nahe_whatsapp_web.nahe_whatsapp_web'].search([]),
#         })

#     @http.route('/nahe_whatsapp_web/nahe_whatsapp_web/objects/<model("nahe_whatsapp_web.nahe_whatsapp_web"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nahe_whatsapp_web.object', {
#             'object': obj
#         })
