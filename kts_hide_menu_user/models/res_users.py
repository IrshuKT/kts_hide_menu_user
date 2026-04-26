from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    # Keep old field if you still want manual override per user
    hide_menu_ids = fields.Many2many(
        comodel_name='ir.ui.menu',
        relation='res_users_hide_menu_rel',
        column1='user_id',
        column2='menu_id',
        string='Hidden Menus',
    )

    menu_profile_id = fields.Many2one(
        comodel_name='kts.menu.profile',
        string='Menu Profile',
        help='Assign a profile to restrict visible menus for this user.',
    )

    def write(self, vals):
        result = super().write(vals)
        if 'hide_menu_ids' in vals or 'menu_profile_id' in vals:
            self.env.registry.clear_cache()
        return result