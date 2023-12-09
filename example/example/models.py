from otree.api import (
    models,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as Cu,
)

author = 'Sophie'

doc = """
Questions on Life and Ethics
"""


class Constants(BaseConstants):
    name_in_url = 'example'
    salary = Cu(8000)
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(min=18, max=100, label="How old are you?")
    chocolate = models.LongStringField(label="Do you like chocolate? Why or why not?")
    altruism = models.CurrencyField(min=0, max=Constants.salary, label=
    "How much of your salary would you give to a random stranger asking you for money for their ticket back home?")
