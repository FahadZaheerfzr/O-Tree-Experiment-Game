import os
from dotenv import load_dotenv

load_dotenv()
SESSION_CONFIGS = [
    dict(
        name='experiment',
        display_name="Experiment",
        #app_sequence=['questionnaire', 'trust', 'public_goods_simple'],
        app_sequence=[ 'trust', 'public_goods_simple'],
        num_demo_participants=6,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']
OTREE_PRODUCTION = True
OTREE_AUTH_LEVEL= "STUDY"
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1, participation_fee=300, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'Rs.'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = os.getenv('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '8306594188499'

INSTALLED_APPS = ['otree']