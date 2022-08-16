from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Questionnaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    understand_drop = models.BooleanField(
        label='I have read the above information. I have asked any questions I had regarding the experimental procedure and they have been answered to my satisfaction. I consent to participate in this study.',
        widget=widgets.CheckboxInput)
    
    age = models.IntegerField(label='What is your age?', min=13, max=125)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    religion = models.StringField(
        choices=[['Muslim', 'Muslim'], ['Hindu', 'Hindu'], ['Atheist', 'Atheist'], ['Jew', 'Jew'], ['Christian', 'Christian']],
        label='What is your religion?',
        widget=widgets.RadioSelect,
    )
    religion_teachings = models.StringField(
        choices=[['Yes', 'Yes'], ['No', 'No'], ['Not Sure', 'Not Sure'], ['N/A', 'N/A']],
        label='Do you consider yourself to be committed to your religious teachings?',
        widget=widgets.RadioSelect,
    )
    religious = models.StringField(
        choices=[['Not religious', 'Not religious'], ['Slightly religious', 'Slightly religious'], 
        ['Moderately religious', 'Moderately religious'], ['Very religious', 'Very religious'],
         ['Don\'t know', 'Don\'t know']],
        label='To what level, do you consider yourself to be religious?',
        widget=widgets.RadioSelect,
    )
    religious_cerm = models.StringField(
        choices=[['Never', 'Never'], ['Less than once a year', 'Less than once a year'], 
        ['Once or twice a year', 'Once or twice a year'], ['Several times a year', 'Several times a year'],
         ['Once a month', 'Once a month'], ['2-3 times a month', '2-3 times a month'],
         ['About once a week', 'About once a week'], ['Several times a week', 'Several times a week']],
        label='How many times do you attend religious services or ceremonies at your place of worship?',
        widget=widgets.RadioSelect,
    )
    religion_scriptures = models.StringField(
        choices=[['Yes', 'Yes'], ['No', 'No'], ['Don\'t know', 'Don\'t know']],
        label='Have you ever read the religious scriptures of the religion you follow? (Bible, Qur’an, Torah, Bhagavad-gita)',
        widget=widgets.RadioSelect,
    )
    describe_God = models.StringField(
        choices=[['Ever-present', 'Ever-present'], ['Critical', 'Critical'], ['Punishing', 'Punishing'],
        ['Wrathful', 'Wrathful'], ['Distant', 'Distant'], ['Forgiving', 'Forgiving'], ],
        label='In your opinion, how will you describe God?',
        widget=widgets.RadioSelect,
    )
    place_after_death = models.StringField(
        choices=[['Yes', 'Yes'], ['No', 'No'], ['Don\'t know', 'Don\'t know']],
        label='Do you believe there is a place for people after death, who have done good deeds (Heaven) and for those who have done bad (Hell)?',
        widget=widgets.RadioSelect,
    )
    heaven = models.StringField(
        choices=[['Definitely', 'Definitely'], ['Maybe', 'Maybe'], ['Not Sure', 'Not Sure'],
         ['Not at all', 'Not at all'], ['I don\'t believe in Heaven', 'I don\'t believe in Heaven']],
        label='Do you think you will go to heaven?',
        widget=widgets.RadioSelect,
    )
    turn_to_religion = models.StringField(
        choices=[['Never', 'Never'], ['Rarely', 'Rarely'], ['Sometimes', 'Sometimes'],
         ['Often', 'Often'], ['Always', 'Always']],
        label='How often do you turn to your religion to help you deal with problems in your life?',
        widget=widgets.RadioSelect,
    )
    city = models.StringField(
        label='Your city'   
    )
    country = models.StringField(
        label='Your country'   
    )
    education = models.StringField(
        choices=[['< 12 years', '<  12 years'], ['= 12 years', '=  12 years'], 
        ['= 14 years', '=  14 years'], ['= 16 years', '=  16 years'],
         ['= 18 years', '= 18 years'], ['> 18 years', '> 18 years']],
        label='Your education',
        widget=widgets.RadioSelect,
    )
    major = models.StringField(
        label='Your major subject'   
    )
    uni = models.StringField(
        label='Your university'   
    )
    cgpa = models.StringField(
        choices=[['< 2', '< 2'], ['2-2.5', '2-2.5'], ['2.5-3', '2.5-3'],
         ['3-3.5', '3-3.5'], ['3.5-4', '3.5-4']],
        label='Your cgpa',  
        widget=widgets.RadioSelect,
    )
    economic_state = models.IntegerField(
        label='Please indicate your Economic State on the scale of 1 to 6, 1 being poor, 6 being rich.',
        max=6,
        min=1
    )
    trusted = models.IntegerField(
        label='Do you think most people can be trusted? Rate on a scale of 0 to 10(0 highly disagree, 10 highly agree)',
        max=10,
        min=0
    )
    

class Questionnaire(Page):
    form_model = 'player'
    form_fields = [ 'age', 'gender', 'religion', 'religion_teachings', 'religious', 'religious_cerm',
    'religion_scriptures', 'describe_God', 'place_after_death', 'heaven', 'turn_to_religion', 'city',
    'country', 'education', 'major', 'uni', 'cgpa', 'economic_state', 'trusted']
    

class Welcome(Page):
    pass

class TermsAndCondition(Page):
    form_model = 'player'
    form_fields = [ 'understand_drop']


page_sequence = [Welcome, TermsAndCondition, Questionnaire]
