# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Nahe_whatsapp_web",
    "summary": """
        Whatsapp Web settings for odoo 16""",
    "author": "Nahe Consulting Group",
    "maintainers": ["nahe-consulting-group"],
    "website": "https://nahe.com.ar/",
    "license": "AGPL-3",
    "category": "Extra Tools",
    "version": "15.0.3.3.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "depends": ["base", "sale", "account"],
    "data": [
        "security/ir.model.access.csv",
        "views/whatsapp_settings_views.xml",
        "views/whatsapp_settings_data.xml",
        "views/buttons_sale_order_views.xml",
        "views/buttons_account_move_views.xml",
        "views/buttons_purchase_order_views.xml",
    ],
}
