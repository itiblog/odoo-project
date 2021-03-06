#-*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 OpenERP SA (<http://openerp.com>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api
from num2words import num2words

class SampleDevelopmentReport(models.AbstractModel):
    _name = 'report.order_conformation_invoice.module_report'

    @api.model
    def render_html(self,docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('order_conformation_invoice.module_report')
        records = self.env['account.invoice'].browse(docids)

        temple_ids = []
        for x in records.invoice_line_ids:
            if x.product_id.product_tmpl_id not in temple_ids:
                temple_ids.append(x.product_id.product_tmpl_id)

        temple_records = []
        def temple_products(prod_id, attrib):
            del temple_records[:]
            current_prod = prod_id
            for x in records.invoice_line_ids:
                if x.product_id.product_tmpl_id == prod_id:
                    temple_records.append(x)
            
            if attrib == "style":
                style_no = ' '
                for x in temple_records:
                    style_no = x.product_id.style_no
                return style_no

            if attrib == "name":
                prod_name = ' '
                for x in temple_records:
                    prod_name = x.product_id.name
                return prod_name

            if attrib == "color":
                prod_color = ' '
                color_list = []
                for x in temple_records:
                    if x.product_id.product_tmpl_id == current_prod:
                        for y in x.product_id.attribute_value_ids:
                            if y.attribute_id.name == "color":
                                if prod_color == ' ':
                                    color_list.append(y.name)
                                    prod_color = y.name
                                else:
                                    if y.name not in color_list:
                                        color_list.append(y.name)
                                        prod_color = prod_color + ', ' + y.name
                return prod_color

            if attrib == "qty":
                prod_qty = 0
                for x in temple_records:
                    if x.product_id.product_tmpl_id == current_prod:
                        prod_qty = prod_qty + x.quantity
                return prod_qty

            if attrib == "avg_price":
                avg_price = 0
                total_price = 0
                list_size = len(temple_records)
                for x in temple_records:
                    total_price = total_price + x.price_unit
                avg_price = total_price/list_size
                return int(avg_price)

            if attrib == "total_price":
                total_price = 0
                for x in temple_records:
                    total_price = total_price + x.price_subtotal/100
                return total_price

            if attrib == "small_size":
                size = 0
                for x in temple_records:
                    for y in x.product_id.attribute_value_ids:
                        if y.name == "s":
                            size = size + x.quantity
                return size

            if attrib == "medium":
                size = 0
                for x in temple_records:
                    for y in x.product_id.attribute_value_ids:
                        if y.name == "m":
                            size = size + x.quantity
                return size

            if attrib == "large":
                size = 0
                for x in temple_records:
                    for y in x.product_id.attribute_value_ids:
                        if y.name == "l":
                            size = size + x.quantity
                return size

            if attrib == "xtra_large":
                size = 0
                for x in temple_records:
                    for y in x.product_id.attribute_value_ids:
                        if y.name == "xl":
                            size = size + x.quantity
                return size

            if attrib == "xx_large":
                size = 0
                for x in temple_records:
                    for y in x.product_id.attribute_value_ids:
                        if y.name == "xxl":
                            size = size + x.quantity
                return size

            if attrib == "xxx_large":
                size = 0
                for x in temple_records:
                    for y in x.product_id.attribute_value_ids:
                        if y.name == "3xl":
                            size = size + x.quantity
                return size



        docargs = {
            'doc_ids': docids,
            'doc_model': 'account.invoice',
            'docs': records,
            'data': data,
            'temple_ids': temple_ids,
            'temple_products': temple_products
            }

        return report_obj.render('order_conformation_invoice.module_report', docargs)

##################### to install num2words ################################
##################### pip install num2words ################################


class Num2Words(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def convert_amount(self):
        word = num2words(self.amount_total)
        word = word.title() + " " + "Only"
        return word