# -*- coding: utf-8 -*-

from odoo import models, fields, api

class devices(models.Model):
	
    _name = 'devices.devices'
    _inherit = 'mail.thread'

    asset_number = fields.Char(string="asset number")
    category_id = fields.Many2one('devices.category', string="category")
    name = fields.Char(string="devices name")
    date = fields.Date(string="purchase date")
    price = fields.Integer(string="price")
    department = fields.Char(string="department")
    user_name = fields.Many2one('res.users', string='user name', track_visibility='onchange')
    location = fields.Char(string="location")
    status = fields.Selection([
    ('using','using'),
    ('idle','idle'),
    ('scrapped','scrapped'),
    ('unknown','unknown')
    ],string="status")
    netwrok = fields.Selection([
    ('intranet','Intranet'),
    ('extranet','Extranet')
    ],string="netwrok", track_visibility='onchange')
    devices_features = fields.Text(string="features")
    notes = fields.Text(string="notes")

class devicescategory(models.Model):
	
	  _name = 'devices.category'
	  _description = "devices category"
	  
	  name = fields.Char(string="category name", required=True)
#	  category_ids = fields.One2many('devices.devices', 'category_id', string='Category ids')