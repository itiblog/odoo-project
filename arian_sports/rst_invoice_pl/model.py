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
from datetime import date


class SampleDevelopmentReport(models.AbstractModel):
    _name = 'report.rst_invoice_pl.module_report'

    @api.model
    def render_html(self,docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('rst_invoice_pl.module_report')
        records = self.env['commercial.packing.list'].browse(docids)

        carton_list = []
        for x in records.commercial_packing_list_tree_link:
            if x.carton not in carton_list:
                carton_list.append(x.carton)

        active_carton = []
        def values(cart_id,attr):
            del active_carton [:]
            cart_id = cart_id
            for x in records.commercial_packing_list_tree_link:
                if x.carton == cart_id:
                    active_carton.append(x)

            if attr == 'style':
                style = ' '
                style_list = []
                for x in active_carton:
                    if x.prod_name.style_no:
                        if style == ' ':
                            style = x.prod_name.style_no
                            style_list.append(x.prod_name.style_no)
                        else:
                            if x.prod_name.style_no not in style_list:
                                style = style + ', ' + x.prod_name.style_no
                                style_list.append(x.prod_name.style_no)
                return style

            if attr == 'color':
                color = ' '
                color_list = []
                for x in active_carton:
                    if x.colour.name:
                        if color == ' ':
                            color = x.colour.name
                            color_list.append(x.colour.name)
                        else:
                            if x.colour.name not in color_list:
                                color = color + ' / ' + x.colour.name
                                color_list.append(x.colour.name)
                return color

            if attr == 'XS':
                size_qty = 0
                size = 'XS'
                for x in active_carton:
                    if x.size.name:
                        if x.size.name == attr:
                            size_qty = size_qty + x.qty
                return size_qty

            if attr == 'S':
                size_qty = 0
                size = 'S'
                for x in active_carton:
                    if x.size.name:
                        if x.size.name == attr:
                            size_qty = size_qty + x.qty
                return size_qty

            if attr == 'M':
                size_qty = 0
                size = 'M'
                for x in active_carton:
                    if x.size.name:
                        if x.size.name == attr:
                            size_qty = size_qty + x.qty
                return size_qty 

            if attr == 'L':
                size_qty = 0
                size = 'L'
                for x in active_carton:
                    if x.size.name:
                        if x.size.name == attr:
                            size_qty = size_qty + x.qty
                return size_qty 

            if attr == 'XL':
                size_qty = 0
                size = 'XL'
                for x in active_carton:
                    if x.size.name:
                        if x.size.name == attr:
                            size_qty = size_qty + x.qty
                return size_qty 

            if attr == 'XXL':
                size_qty = 0
                size = 'XXL'
                for x in active_carton:
                    if x.size.name:
                        if x.size.name == attr:
                            size_qty = size_qty + x.qty
                return size_qty

            if attr == '3XL':
                size_qty = 0
                size = '3XL'
                for x in active_carton:
                    if x.size.name:
                        if x.size.name == attr:
                            size_qty = size_qty + x.qty
                return size_qty 

            if attr == 'GW':
                G_W = 0
                for x in active_carton:
                    if x.gross_weight:
                        G_W = G_W + x.gross_weight
                return G_W

            if attr == 'NW':
                N_W = 0
                for x in active_carton:
                    if x.net_weight:
                        N_W = N_W + x.net_weight
                return N_W              


        docargs = {
            'doc_ids': docids,
            'doc_model': 'commercial.packing.list',
            'docs': records,
            'data': data,
            'carton_list':carton_list,
            'values':values,
            }

        return report_obj.render('rst_invoice_pl.module_report', docargs)
