from odoo import api, fields, models, _


class CrossoveredBudgetLines(models.Model):
    _inherit = "crossovered.budget.lines"

    difference = fields.Float(string="Difference", compute='compute_difference_value')
    difference_perc = fields.Float(string="Difference Percentage", compute='compute_difference_value')

    @api.depends('planned_amount', 'practical_amount')
    def compute_difference_value(self):
        for rec in self:
            if rec.planned_amount and rec.practical_amount:
                rec.difference = rec.planned_amount - rec.practical_amount
                #rec.difference_perc = float((rec.practical_amount / rec.planned_amount) * 100) / 100
                rec.difference_perc = float(((rec.planned_amount - rec.practical_amount))/rec.practical_amount ) /100

            else:
                rec.difference = False
                rec.difference_perc = False


