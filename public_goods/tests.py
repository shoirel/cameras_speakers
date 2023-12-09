from otree.api import Currency as cu, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield Contribute, dict(contribution=cu(1))
        yield