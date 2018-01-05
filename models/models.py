# -*- coding: utf-8 -*-

from odoo import models, fields, api

class devices(models.Model):
	
    _name = 'devices.devices'
    _inherit = 'mail.thread'

    asset_number = fields.Char(string="asset number", track_visibility='onchange')
    category_id = fields.Many2one('devices.category', string="category", track_visibility='onchange')
    name = fields.Char(string="devices name", track_visibility='onchange')
    date = fields.Date(string="purchase date", track_visibility='onchange')
    price = fields.Integer(string="price", track_visibility='onchange')
    department = fields.Many2one('devices.department', string="department", track_visibility='onchange')
    user_name = fields.Many2one('devices.users', string="users name", track_visibility='onchange')
    location = fields.Many2one('devices.location', string="location", track_visibility='onchange')
    status = fields.Selection([
    ('using','using'),
    ('idle','idle'),
    ('scrapped','scrapped'),
    ('unknown','unknown')
    ],string="status", track_visibility='onchange')
    netwrok = fields.Selection([
    ('intranet','Intranet'),
    ('extranet','Extranet')
    ],string="netwrok", track_visibility='onchange')
    devices_features = fields.Text(string="features", track_visibility='onchange')
    use_records = fields.Text(string="use records", track_visibility='onchange')
    notes = fields.Text(string="notes", track_visibility='onchange')
    
class devices(models.Model):
	  
	  _name = 'devices.dongle'
	  _description = "devices dongle"
	  _inherit = 'mail.thread'
	  
	  name = fields.Char(string="devices name", track_visibility='onchange')
	  user_name = fields.Many2one('dongle.users', string="users name", track_visibility='onchange')
	  asset_number = fields.Char(string="asset number", track_visibility='onchange')
	  borrow_date = fields.Date(string="borrow date", track_visibility='onchange')
	  return_date = fields.Date(string="return date", track_visibility='onchange')
	  use = fields.Char(string="use", track_visibility='onchange')
	  recipients = fields.Many2one('dongle.users', string="recipients", track_visibility='onchange')
	  notes = fields.Text(string="notes", track_visibility='onchange')
	  use_records = fields.Text(string="use records", track_visibility='onchange')

class devicescategory(models.Model):
	
	  _name = 'devices.category'
	  _description = "devices category"
	  
	  name = fields.Char(string="category name", required=True)

class devicesusers(models.Model):
	
	  _name = 'devices.users'
	  _description = "devices users"
	  
	  name = fields.Char(string="users name", required=True)
	  
class dongleusers(models.Model):
	
	  _name = 'dongle.users'
	  _description = "dongle users"
	  
	  name = fields.Char(string="users name", required=True)

class devicesdepartment(models.Model):
	
	  _name = 'devices.department'
	  _description = "devices department"
	  
	  name = fields.Char(string="department", required=True)

class deviceslocation(models.Model):
	
	  _name = 'devices.location'
	  _description = "devices location"
	  
	  name = fields.Char(string="location", required=True)