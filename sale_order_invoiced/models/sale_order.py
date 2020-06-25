# -*- coding: utf-8 -*-

from odoo import models, fields, api

class sale_order_invoiced(models.Model):
    _inherit = 'sale.order'

    invoiced = fields.Boolean(string="Invoiced")


    @api.multi
    def set_order_invoiced(self):
        for sale in self:
            sale.invoiced = True

    @api.depends('state', 'order_line.invoice_status', 'order_line.invoice_lines','invoiced')
    def _get_invoiced(self):
        for rec in self:
            sale = super(sale_order_invoiced, rec)._get_invoiced()
            if rec.invoiced:
                rec.invoice_status = 'invoiced'
            return sale
