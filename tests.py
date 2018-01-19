from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
import random


# **********************************************************************************************************************
# *** BOT
# **********************************************************************************************************************
class PlayerBot(Bot):

    def play_round(self):

        # ------------------------------------------------------------------------------------------------------------ #
        # submit instructions page
        # ------------------------------------------------------------------------------------------------------------ #
        if Constants.instructions:
            yield (views.Instructions)

        # ------------------------------------------------------------------------------------------------------------ #
        # make decisions
        # ------------------------------------------------------------------------------------------------------------ #
        num_lotteries = Constants.num_lotteries + 1 if Constants.risk_loving else Constants.num_lotteries
        yield (views.Decision, {'lottery_choice': random.randint(1, num_lotteries)})

        # ------------------------------------------------------------------------------------------------------------ #
        # submit results page
        # ------------------------------------------------------------------------------------------------------------ #
        if Constants.results:
            yield (views.Results)