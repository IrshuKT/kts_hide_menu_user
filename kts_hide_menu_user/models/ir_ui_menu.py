from odoo import models, api


class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    def _filter_visible_menus(self):
        """Override to additionally hide menus configured per user.

        _filter_visible_menus runs AFTER _visible_menu_ids cache,
        so it's safe to access self.env.user here with no cache issues.
        """
        menus = super()._filter_visible_menus()

        user = self.env.user

        # Admins always see everything
        if user._is_admin():
            return menus

        hidden_ids = set(user.hide_menu_ids.ids)
        if not hidden_ids:
            return menus

        return menus.filtered(lambda m: m.id not in hidden_ids)