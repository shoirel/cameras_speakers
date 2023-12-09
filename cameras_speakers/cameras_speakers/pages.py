from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import re


class Intro(Page):
    form_model = 'player'

    def is_displayed(self):
        return True

    def get_form_fields(self):
        set = ['satisfied', 'rec_kept', 'like', 'enjoy', 'clarity', 'connection', 'easiness', 'reflections',
               ]
        return set


class Q1(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        set = ['assess1', 'assess1_txt', 'gpt'
               ]
        return set


class Q2(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        set = ['assess2', 'assess2_txt', 'gpt2'
               ]
        return set


class Q3(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        set = ['assess3', 'assess3_txt', 'gpt3'
               ]
        return set


class Q4(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        set = ['assess4', 'assess4_txt', 'gpt4'
               ]
        return set


class Q5(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        set = ['assess5', 'assess5_txt', 'gpt5'
               ]
        return set


class Q6(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        set = ['assess6', 'assess6_txt', 'gpt6'
               ]
        return set


class Q7(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        set = ['assess7', 'assess7_txt', 'gpt7'
               ]
        return set


class Fake(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        add = ['cameras']
        return add


class Project(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        add = ['cameras_good', 'no_guess']
        return add


class Guess_ON(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        on = ['guess1', 'guess2', 'guess3', 'guess4', 'guess5']
        return on

    def is_displayed(self):
        if self.player.no_guess == True and self.player.participant.vars['treatment'][0] == "ON_FIRST":
            return True


class Guess_OFF(Page):
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


page_sequence = [Intro, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Fake, Project, Guess_OFF, Guess_ON, Thanks]
