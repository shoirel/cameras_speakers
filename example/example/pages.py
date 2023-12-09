from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Hello(Page):
    form_model = 'player'
    form_fields = ['age', 'chocolate', 'altruism']

    def vars_for_template(self):
        salary = Constants.salary
        return dict(
            salary=salary,
        )


class Judgement(Page):

    def vars_for_template(self):
        salary = Constants.salary
        left = salary - self.player.altruism
        if salary - left > salary / 10:
            judgement = "Nice"
        else:
            judgement = "Not nice"
        return dict(
            salary=salary,
            left=left,
            judgement=judgement,
        )


class Thanks(Page):
    form_model = 'player'


page_sequence = [Hello, Judgement, Thanks]
