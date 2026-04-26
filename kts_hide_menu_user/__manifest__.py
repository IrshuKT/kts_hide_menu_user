{
    'name': 'Hide Menu User Wise',
    'version': '19.0.1.1.0',
    'category': 'Tools',
    'summary': 'Hide specific menus for specific users',
    'description': """
        This module allows administrators to hide specific menus 
        (main menus and submenus) for individual users.
        
        Features:
        - Hide any menu/submenu per user
        - Simple configuration from the user form
        - Works with Odoo 19 Enterprise & Community
        - No restart required — changes are immediate
    """,
    'author': 'Irshad K T',
    'website':'www.linkedin.com/in/irshadkt',
    'images':['static/description/banner.gif]',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_users_views.xml',
        'views/menu_profile_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
