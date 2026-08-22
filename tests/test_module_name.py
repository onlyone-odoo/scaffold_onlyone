# Copyright 2026 Be OnlyOne
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestModuleName(TransactionCase):
    """Replace with real tests; keep post_install for localization/account."""

    def test_module_installed(self):
        module = self.env["ir.module.module"].search(
            [("name", "=", "module_name")],
            limit=1,
        )
        self.assertEqual(module.state, "installed")
