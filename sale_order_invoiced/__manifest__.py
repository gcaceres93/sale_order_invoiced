# -*- coding: utf-8 -*-
{
    'name': "sale_order_invoiced",

    'summary': """
        For mark the sale order as invoiced without  sale order lines invoiced logic""",

    'description': """
    """,

    'author': "SATI",
    'website': "http://sati.com.py",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_views.xml',
    ],

}