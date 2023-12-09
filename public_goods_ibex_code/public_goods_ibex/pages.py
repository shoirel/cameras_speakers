from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']
    def vars_for_template(self):
        PLAYERS_PER_GROUP = Constants.players_per_group
        ENDOWMENT = Constants.endowment
        MULTIPLIER = Constants.multiplier

        return dict(
            PLAYERS_PER_GROUP=PLAYERS_PER_GROUP,
            ENDOWMENT=ENDOWMENT,
            MULTIPLIER=MULTIPLIER,
        )


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):

    def vars_for_template(self):
        ENDOWMENT = Constants.endowment
        left = ENDOWMENT - self.player.contribution
        individual_earnings = self.group.total_contribution * Constants.multiplier / 3
        return dict(
            ENDOWMENT=ENDOWMENT,
            left=left,
            individual_earnings=individual_earnings,
        )


    pass

class Contribute_2(Page):
    form_model = 'player'
    form_fields = ['contribution_2']
    def vars_for_template(self):
        PLAYERS_PER_GROUP = Constants.players_per_group
        ENDOWMENT = Constants.endowment
        MULTIPLIER = Constants.multiplier

        return dict(
            PLAYERS_PER_GROUP=PLAYERS_PER_GROUP,
            ENDOWMENT=ENDOWMENT,
            MULTIPLIER=MULTIPLIER,
        )

class ResultsWaitPage_2(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs_2()

class Results_2(Page):

    def vars_for_template(self):
        ENDOWMENT = Constants.endowment
        left = ENDOWMENT - self.player.contribution_2
        individual_earnings = self.group.total_contribution_2 * Constants.multiplier / 3
        return dict(
            ENDOWMENT=ENDOWMENT,
            left=left,
            individual_earnings=individual_earnings,
        )

    pass


class Contribute_3(Page):
    form_model = 'player'
    form_fields = ['contribution_3']

    def vars_for_template(self):
        PLAYERS_PER_GROUP = Constants.players_per_group
        ENDOWMENT = Constants.endowment
        MULTIPLIER = Constants.multiplier

        return dict(
            PLAYERS_PER_GROUP=PLAYERS_PER_GROUP,
            ENDOWMENT=ENDOWMENT,
            MULTIPLIER=MULTIPLIER,
        )

class ResultsWaitPage_3(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs_3()

class Results_3(Page):

    def vars_for_template(self):
        ENDOWMENT = Constants.endowment
        left = ENDOWMENT - self.player.contribution_3
        individual_earnings = self.group.total_contribution_3 * Constants.multiplier / 3
        return dict(
            ENDOWMENT=ENDOWMENT,
            left=left,
            individual_earnings=individual_earnings,
        )

    pass

class Thanks(Page):
    form_model = 'player'


page_sequence = [Contribute, ResultsWaitPage, Results, Contribute_2, ResultsWaitPage_2, Results_2,
                 Contribute_3, ResultsWaitPage_3, Results_3, Thanks]
