from secrets import choice
from otree.api import *
import random


class C(BaseConstants):
    NAME_IN_URL = 'public_goods_simple'
    PLAYERS_PER_GROUP = 6
    NUM_ROUNDS = 1
    MULTIPLIER = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


class Player(BasePlayer):
    choice = models.IntegerField(
        choices=[[0,'KEEP all the money' ], 
        [1, 'PUT half the money in public pool']],
        label="What would you like to do with your Money?",
        widget=widgets.RadioSelect,
    )
    phone_number = models.StringField()
    account_number = models.StringField()
    name=models.StringField()
    CNIC = models.StringField(label="CNIC")
    recitation = models.BooleanField()


# FUNCTIONS
def set_payoffs(group: Group):
    players = group.get_players()
    contributions = []
    for p in players:
        if p.choice == 0:
            contributions.append(cu(0))
        else:
            contributions.append(cu(p.participant.payoff_plus_participation_fee()/2))
    print(contributions)
    group.total_contribution = sum(contributions)
    group.individual_share = (
        group.total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP
    )
    i = 0
    for p in players:
        p.participant.payoff = ((p.participant.payoff_plus_participation_fee() - contributions[i] + group.individual_share - 300) )
        i+=1
        print(p.participant.payoff_plus_participation_fee())


# PAGES

class Recitation(Page):
    @staticmethod
    def is_displayed(player):
        player.recitation = False
        displayed = random.randint(0,1)
        print(displayed)
        if displayed == 1:
            player.recitation = True

        return displayed == 1

class Introduction(Page):
    form_model = 'player'


class Contribute(Page):
    form_model = 'player'
    form_fields = ['choice']

    @staticmethod
    def vars_for_template(player: Player):
        earned_money = player.participant.payoff.to_real_world_currency(player.session)
        return dict(earned_money=earned_money)


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    form_model = 'player'
    form_fields = ['name', 'CNIC','phone_number', 'account_number']


class Thanks(Page):
    pass


page_sequence = [Introduction, Recitation, Contribute, ResultsWaitPage, Results, Thanks]
