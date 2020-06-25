# -*- coding: utf-8 -*-

from odoo import models, fields, api

class purchase_order_line(models.Model):
    _inherit = 'purchase.order.line'

    @api.depends('invoice_lines.invoice_id.state', 'invoice_lines.quantity')
    def _compute_qty_invoiced(self):
        for rec in self:
                purchase = super(purchase_order_line, rec)._compute_qty_invoiced()
                if rec.order_id.invoice_status == 'invoiced':
                    rec.qty_invoiced = rec.product_qty
                return purchase


class purchase_order_invoiced(models.Model):
    _inherit = 'purchase.order'

    invoiced = fields.Boolean(string="Invoiced")


    @api.multi
    def set_order_invoiced(self):
        for sale in self:
            sale.invoice_status = 'invoiced'

