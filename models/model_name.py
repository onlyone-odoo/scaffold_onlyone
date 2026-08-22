# Copyright 2026 Be OnlyOne
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ModelName(models.Model):
    _name = "model.name"
    _description = "Model Name"

    @api.model
    def _default_company_id(self):
        """Return the current company."""
        return self.env.company

    name = fields.Char(required=True)
    company_id = fields.Many2one(
        comodel_name="res.company",
        required=True,
        ondelete="restrict",
        default="_default_company_id",
    )
