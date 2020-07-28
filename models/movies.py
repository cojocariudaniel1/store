from odoo import fields, models, api

class movie(models.Model):
    _name = 'test13.movie'
    _description = 'Movies'

    name = fields.Char ('Movie Name:', required= True)
    launch_date= fields.Date('Launch Date:')
    description_movie= fields.Text('Description:')
    poster= fields.Image('Poster of the Movie:')
    deposit= fields.Integer('Copies of Movie In Deposit')
    price= fields.Monetary('Price:', group_operator='avg')
    rate= fields.Float('Rate:')
    category= fields.Char('Category:')
    currency_id= fields.Many2many('test13.store', string= 'Price')
    actor_ids = fields.Many2many("test13.cast", string= 'Actors:')

    def button_action1(self):
        return {
            'name':'Movie',
            'view_mode': 'form',
            'view_id': False,
            'view_type': 'form',
            'res_model': 'ir.ui.view',
            'type': 'ir.actions.act_window',
            'nodestroy': True,
            'target': 'current',
            'domain': '[]',

}

