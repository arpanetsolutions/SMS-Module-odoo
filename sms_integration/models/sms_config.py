from odoo import api, fields, models

class sms_config(models.Model):

	_name = "sms.config"
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	_description = "Sms Configuration"
	_rec_name = "user_name"

	user_name = fields.Char(string="UserName", required=True)
	password = fields.Char(string="Password", required=True)
	sender_name = fields.Char(string="Sender ID",required=True)