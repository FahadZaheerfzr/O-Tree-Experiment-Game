from turtle import pd
from otree.api import *

doc = """
This is a standard 2-player trust game where the amount sent by player 1 gets
tripled. The trust game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""

li = []

class C(BaseConstants):
    NAME_IN_URL = 'trust'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    INSTRUCTIONS_TEMPLATE = 'trust/instructions.html'
    # Initial amount allocated to each player
    ENDOWMENT = cu(200)
    MULTIPLIER = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.IntegerField(
        choices=[[200,'Keep 0 experimental points, send 200 Experimental points to the Second Mover.' ], 
        [0, 'Keep 200 experimental points, send 0 Experimental points to the Second Mover.']],
        doc="""Amount sent by P1""",
        label="What would you like to do?",
        widget=widgets.RadioSelect)
    sm_kept_amount = models.IntegerField(
        choices=[[400,'Keep 400 experimental points, send 0 Experimental points.' ], 
        [230, 'Send 250 Experimental points, and keep 230 experimental points.']],
        doc="""Amount sent back by P2""",
        label="You have two choices",
        widget=widgets.RadioSelect,
        initial = 0,
        blank=True)


class Player(BasePlayer):
    pass


# FUNCTIONS
def sent_back_amount_max(group: Group):
    return group.sent_amount * C.MULTIPLIER



# PAGES
class Introduction(Page):
    pass

class BeforeSend(WaitPage):
    pass

class Send(Page):
    """This page is only for P1
    P1 sends amount (all, some, or none) to P2
    This amount is tripled by experimenter,
    i.e if sent amount by P1 is 5, amount received by P2 is 15"""

    form_model = 'group'
    form_fields = ['sent_amount']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1


class SendBackWaitPage(WaitPage):
    pass


class SendBack(Page):
    """This page is only for P2
    P2 sends back some amount (of the tripled amount received) to P1"""

    form_model = 'group'
    form_fields = ['sm_kept_amount']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2
    '''
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group

        tripled_amount = group.sent_amount * C.MULTIPLIER
        return dict(tripled_amount=tripled_amount)'''


class ResultsWaitPage(WaitPage):
    wait_for_all_groups = True
    @staticmethod
    def after_all_players_arrive(subsession:Subsession):
        
        fm_senders = 0
        fm_keepers = 0
        sm_senders = 0
        sm_keepers = 0
        for g in subsession.get_groups():
            if g.sent_amount == 200:
                fm_senders += 1
                if g.sm_kept_amount == 400:
                    sm_keepers += 1
                else:
                    sm_senders += 1
            else:
                fm_keepers += 1
        FM_SENT_PERCENTAGE = fm_senders / (fm_keepers+fm_senders) * 100
        FM_SENT_PERCENTAGE = round(FM_SENT_PERCENTAGE, 3)
        
        FM_KEPT_PERCENTAGE = fm_keepers / (fm_keepers+fm_senders) * 100
        FM_KEPT_PERCENTAGE = round(FM_KEPT_PERCENTAGE, 3)
        
        SM_KEPT_PERCENTAGE = sm_keepers / (fm_keepers+fm_senders) * 100
        SM_KEPT_PERCENTAGE = round(SM_KEPT_PERCENTAGE, 3)
        
        SM_SENT_PERCENTAGE = sm_senders / (fm_keepers+fm_senders) * 100
        SM_SENT_PERCENTAGE = round(SM_SENT_PERCENTAGE, 3)
        
        SM_NOT_RECIEVED = fm_keepers / (fm_keepers+fm_senders) * 100
        SM_NOT_RECIEVED = round(SM_NOT_RECIEVED, 3)

        li.append(FM_SENT_PERCENTAGE)
        li.append(FM_KEPT_PERCENTAGE)
        li.append(SM_KEPT_PERCENTAGE)
        li.append(SM_SENT_PERCENTAGE)
        li.append(SM_NOT_RECIEVED)
        

    

class Results(Page):
    """This page displays the earnings of each player"""
    @staticmethod
    def vars_for_template(player: Player):
        if player.id_in_group == 1:
            player.payoff = 200-player.group.sent_amount
            if player.group.sm_kept_amount == 230:
                player.payoff += 250
        else:
            player.payoff = player.group.sm_kept_amount
        li_key = ["FM_SENT_PERCENTAGE","FM_KEPT_PERCENTAGE","SM_KEPT_PERCENTAGE","SM_SENT_PERCENTAGE",
        "SM_NOT_RECIEVED"]
        return dict(zip(li_key, li))


page_sequence = [
    Introduction,
    BeforeSend,
    Send,
    SendBackWaitPage,
    SendBack,
    ResultsWaitPage,
    Results,
]