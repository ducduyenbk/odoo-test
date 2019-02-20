from odoo import fields, models

class EtgLead(models.Model):
    _inherit = 'crm.lead'

    short_name = fields.Char("Tên viết tắt")
