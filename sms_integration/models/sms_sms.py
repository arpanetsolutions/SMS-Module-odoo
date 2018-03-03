# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import datetime
from datetime import datetime as dt
import requests


class sms_sms(models.TransientModel):

	_name = "sms.sms"
	_description = "Sms Logs"
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	_description = "Send SMS"

	user_id = fields.Many2one("sms.config","Account", required= True)
	message = fields.Text(String="Message", size=140)
	mobile_no = fields.Char(string="Receiver Number", required= True, size=12)
	date_time = fields.Datetime(string="Date & Time",readonly=True, store=True)
	status = fields.Selection([('draft','Draft'),('sent','Sent')],default='draft',string="Status")


	@api.multi
	def process_demo_scheduler_queue(self):
		sms_scheduled_obj = self.env['sms.scheduled'].search([])
		today_date = datetime.date.today()
		for sms in sms_scheduled_obj:
			if type(sms.scheduled_on) == str:
				sms_scheduled_date = datetime.datetime.strptime(sms.scheduled_on, "%Y-%m-%d").date()
				if sms_scheduled_date == today_date:
					self.send_sms_via_schedular(sms)
					

	@api.multi
	def send_sms_via_schedular(self,sms):
		API01 = 'error API01 : Invalid Username or Password.'
		API03 = 'error API03 : Invalid senderid format.'
		API04 = 'error API04 : You have not sufficiant balance.'
		API06 = 'error API06 : Please enter 10 digit mobile number.'
		mobile = '9727152508'
		url = 'http://sms.dynasoft.in/sendsms.aspx'
		sms_config_obj = self.env['sms.config'].search([])
		payload = {
					'mobile': sms_config_obj.user_name, 
					'pass': sms_config_obj.password,
					'senderid':sms_config_obj.sender_name,
					'to': sms.mobile,
					'msg':sms.message,
					'msgtype':'utf-8'
				}
		r = requests.post(url, data=payload)
		if r.text == API01:
			raise ValidationError(_("Invalid Username or Password."))
		elif r.text == API03:
			raise ValidationError(_("Invalid senderid format."))
		elif r.text == API04:
			raise ValidationError(_("You have not sufficiant balance."))
		elif r.text == API06:
			raise ValidationError(_("Please enter 10 digit mobile number."))
		elif r.text == '1 SMS Sent.' and r.status_code == 200:
			self.create({'user_id':sms_config_obj.id,
						'message':sms.message,
						'mobile_no':sms.mobile,
						'date_time':dt.now(),
						'status':'sent'
					})
			sms.write({'status':'sent'})
		else:
			sms.write({'status':'fail'})

	@api.multi
	def send_sms(self):
		API01 = 'error API01 : Invalid Username or Password.'
		API03 = 'error API03 : Invalid senderid format.'
		API04 = 'error API04 : You have not sufficiant balance.'
		API06 = 'error API06 : Please enter 10 digit mobile number.'
		url = 'http://sms.dynasoft.in/sendsms.aspx'
		payload = {
					'mobile': self.user_id.user_name, 
					'pass': self.user_id.password,
					'senderid':self.user_id.sender_name,
					'to':self.mobile_no,
					'msg':self.message,
					'msgtype':'utf-8'
				}
		r = requests.post(url, data=payload)
		r.text
		if r.text == API01:
			raise ValidationError(_("Invalid Username or Password."))
		elif r.text == API03:
			raise ValidationError(_("Invalid senderid format."))
		elif r.text == API04:
			raise ValidationError(_("You have not sufficiant balance."))
		elif r.text == API06:
			raise ValidationError(_("Please enter 10 digit mobile number."))
		elif r.text == '1 SMS Sent.' and r.status_code == 200:
			self.write({'date_time':dt.now(),'status':'sent'})