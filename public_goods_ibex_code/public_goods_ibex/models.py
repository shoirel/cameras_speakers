from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as Cu,
    currency_range,
)

author = 'Sophie'

doc = """
Public Goods Game
"""


class Constants(BaseConstants):
    name_in_url = 'public_goods'
    players_per_group = 3
    num_rounds = 1
    endowment = Cu(100)
    multiplier = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    total_contribution_2 = models.CurrencyField()
    total_contribution_3 = models.CurrencyField()
    individual_share = models.CurrencyField()
    individual_share_2 = models.CurrencyField()
    individual_share_3 = models.CurrencyField()

    def set_payoffs(self):
        players = self.get_players()
        contributions = [p.contribution for p in players]
        self.total_contribution = sum(contributions)
        self.individual_share = (
                self.total_contribution * Constants.multiplier / Constants.players_per_group
        )
        for p in players:
            p.payoff = Constants.endowment - p.contribution + self.individual_share

    def set_payoffs_2(self):
        players = self.get_players()
        contributions_2 = [p.contribution_2 for p in players]
        self.total_contribution_2 = sum(contributions_2)
        self.individual_share_2 = (
                self.total_contribution_2 * Constants.multiplier / Constants.players_per_group
        )
        for p in players:
            p.payoff = Constants.endowment - p.contribution_2 + self.individual_share_2

    def set_payoffs_3(self):
        players = self.get_players()
        contributions_3 = [p.contribution_3 for p in players]
        self.total_contribution_3 = sum(contributions_3)
        self.individual_share_3 = (
                self.total_contribution_3 * Constants.multiplier / Constants.players_per_group
        )
        for p in players:
            p.payoff = Constants.endowment - p.contribution_3 + self.individual_share_3


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=Constants.endowment, label="How much will you contribute?"
    )
    contribution_2 = models.CurrencyField(
        min=0, max=Constants.endowment, label="How much will you contribute?"
    )
    contribution_3 = models.CurrencyField(
        min=0, max=Constants.endowment, label="How much will you contribute?"
    )

    # def set_cumulative_payoffs(self):
    #     players = self.get_players()
    #     for p in players:
    #         p.cumulative_payoff = sum([p.payoff for p in self.player.in_all_rounds()])
