from odoo import models


class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    def _filter_visible_menus(self):
        menus = super()._filter_visible_menus()
        user = self.env.user

        if user._is_admin():
            return menus

        # --- Profile based (whitelist) ---
        if user.menu_profile_id:
            allowed_ids = set(user.menu_profile_id.menu_ids.ids)
            if allowed_ids:
                # Walk up the parent chain for every allowed menu
                # so root and intermediate menus are never blocked
                all_allowed_ids = set()
                menus_to_check = self.env['ir.ui.menu'].browse(allowed_ids)

                for menu in menus_to_check:
                    # Add the menu itself
                    all_allowed_ids.add(menu.id)
                    # Walk up all parents until root
                    parent = menu.parent_id
                    while parent:
                        all_allowed_ids.add(parent.id)
                        parent = parent.parent_id

                return menus.filtered(lambda m: m.id in all_allowed_ids)

        # --- Manual hide (blacklist) fallback ---
        hidden_ids = set(user.hide_menu_ids.ids)
        if hidden_ids:
            return menus.filtered(lambda m: m.id not in hidden_ids)

        return menus