# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CrmLead(models.Model):

	_inherit = 'crm.lead'

	@api.multi
	def open_sms_wizard(self):
		return {
				'name':'Send SMS',
				'res_model':'sms.sms',
				'view_type':'form',
				'view_mode':'form',
				'target':'new',
				'type':'ir.actions.act_window',
				'context': {'default_mobile_no': self.phone}
			}

	@api.multi
	def open_sms_schedular(self):
		return {
				'name':'Schedual SMS',
				'res_model':'sms.scheduled',
				'view_type':'form',
				'view_mode':'form',
				'target':'new',
				'type':'ir.actions.act_window',
				'context': {'default_partner_id':self.partner_id.id,'default_mobile': self.phone}
			}
