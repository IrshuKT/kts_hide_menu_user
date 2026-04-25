from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    hide_menu_ids = fields.Many2many(
        comodel_name='ir.ui.menu',
        relation='res_users_hide_menu_rel',
        column1='user_id',
        column2='menu_id',
        string='Hidden Menus',
        help='Select the menus that should be hidden for this user.',
    )

    def write(self, vals):
        result = super().write(vals)
        if 'hide_menu_ids' in vals:
            # Clear the _visible_menu_ids ormcache so load_menus
            # picks up the new filter on next page load
            self.env.registry.clear_cache()
        return result