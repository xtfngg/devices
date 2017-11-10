# -*- coding: utf-8 -*-
from odoo import http

class devices(http.Controller):
     @http.route('/devices/devices/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/devices/devices/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('devices.listing', {
             'root': '/devices/devices',
             'objects': http.request.env['devices.devices'].search([]),
         })

     @http.route('/devices/devices/objects/<model("devices.devices"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('devices.object', {
             'object': obj
         })