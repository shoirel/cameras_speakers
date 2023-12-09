from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import re


class Welcome(Page):
    form_model = 'player'
    form_fields = ['summary']

    def is_displayed(self):
        return True


class Q1(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        set = ['familiar', 'knowledge', 'like', 'enjoy', 'clarity', 'connection', 'easiness', 'onoff', 'cameras', 'remarks',
               ]
        return set


class Q2(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        add = ['cameras_good', 'no_guess']
        return add


class Q3(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        on = ['guess1', 'guess2', 'guess3', 'guess4', 'guess5']
        return on

    def is_displayed(self):
        if self.player.no_guess == True and self.player.participant.vars['treatment'][0] == "ON_FIRST":
            return True


class Q3_Off(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        off = ['guess1_reversed', 'guess2_reversed', 'guess3_reversed', 'guess4_reversed', 'guess5_reversed']
        return off

    def is_displayed(self):
        if self.player.no_guess == True and self.player.participant.vars['treatment'][0] == "OFF_FIRST":
            return True


class Thanks(Page):
    form_model = 'player'


page_sequence = [Welcome, Q1, Q2, Q3, Q3_Off, Thanks]
