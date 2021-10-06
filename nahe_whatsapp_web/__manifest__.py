# -*- coding: utf-8 -*-
{
    'name': "nahe_whatsapp_web",

    'summary': """
        Generador link con mensaje para enviar por whatsappweb desde odoo.""",

    'description': """
        1º usar whatsapp web es gratis para pequeñas empresas que quieran aprovechar este medio.
        2º desde las ordenes de venta se puede mandarle un mensaje al cliente con un boton, siempre que el numero este correctamente anotado.
        3º en parámetros del sistema se pone el mensaje predeterminado generico. Respetando los datos con # se puede alterar el mensaje.
        4º Ahora tenemos el boton en las ordenes de venta, facturas y ordenes de compra que ayuda a mandar el mensaje por whatsappweb de forma simple.
        5º Se puede modificar facilmente el codigo del modulo para generar más botones en el sistema.

    """,

    'author': "Nähe Consulting Group",
    'website': "http://www.nahe.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
