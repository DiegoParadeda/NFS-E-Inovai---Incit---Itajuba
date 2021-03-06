# -*- coding: utf-8 -*-
from odoo import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['todo.task', 'mail.thread']
    user_id = fields.Many2one('res.users', 'Responsible')
    date_deadline = fields.Date('Deadline')
    name = fields.Char(help="What needs to be done?")
