# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class sms_scheduled(models.Model):

	_name = "sms.scheduled"
	_description = "Schedualed Sms"
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	_rec_name = 'partner_id'

	partner_id = fields.Many2one('res.partner',required= True,string="SMS To")
	mobile = fields.Char(string="Receiver Number", required= True, size=12)
	message = fields.Text(String="Message", required= True, size=140)
	scheduled_on = fields.Date(string="Scheduled On", required= True)
	status = fields.Selection([('draft','Draft'),('fail','Fail'),('sent','Sent')],default='draft',string="Status")


	@api.onchange('partner_id')
	def onchange_partner_id(self):
		if self.partner_id.mobile:
			self.mobile = self.partner_id.mobile