# -*- coding: utf-8 -*-
{
    'name': "compras",

    'summary': """
        Crear ordenes de compras y gestionar los proveedores""",

    'description': """
        Este modulo sera el mejor del mundo
    """,

    'author': "Jesus",
    'website': "jesusgamboad@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view_proveedores.xml',
        'views/view_productos.xml',
        'views/view_orden.xml'
        'views/templates.xml',
      #  'views/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}