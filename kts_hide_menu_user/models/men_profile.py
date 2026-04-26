from odoo import models, fields


class KtsMenuProfile(models.Model):
    _name = 'kts.menu.profile'
    _description = 'Menu Access Profile'

    name = fields.Char(string='Profile Name', required=True)
    menu_ids = fields.Many2many(
        comodel_name='ir.ui.menu',
        relation='kts_menu_profile_menu_rel',
        column1='profile_id',
        column2='menu_id',
        string='Allowed Menus',
        help='Only these menus will be visible to users assigned this profile.',
    )
    user_ids = fields.One2many(
        comodel_name='res.users',
        inverse_name='menu_profile_id',
        string='Users',
    )