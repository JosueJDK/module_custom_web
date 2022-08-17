# -*- coding: utf-8 -*-
# from odoo import http


# class AddDescuentoProduct(http.Controller):
#     @http.route('/add_descuento_product/add_descuento_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_descuento_product/add_descuento_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_descuento_product.listing', {
#             'root': '/add_descuento_product/add_descuento_product',
#             'objects': http.request.env['add_descuento_product.add_descuento_product'].search([]),
#         })

#     @http.route('/add_descuento_product/add_descuento_product/objects/<model("add_descuento_product.add_descuento_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_descuento_product.object', {
#             'object': obj
#         })
