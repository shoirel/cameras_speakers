from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    currency_range,
)

author = 'Sophie'

doc = """
Questionnaire for listeners
"""


class Constants(BaseConstants):
    name_in_url = 'cameras_listeners'
    players_per_group = None
    num_rounds = 1
    TREATMENT = ('ON_FIRST', 'OFF_FIRST')


class Subsession(BaseSubsession):
    def creating_session(self):
        session = self.session
        if self.round_number == 1:
            import random as rnd
            players = self.get_players()
            for p in players:
                TREATMENT = rnd.sample(
                    Constants.TREATMENT, k=len(Constants.TREATMENT))
                p.participant.vars['treatment'] = TREATMENT
                p.TREATMENT = TREATMENT[0]

    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    TREATMENT = models.StringField()
    summary = models.LongStringField(label='', blank=False)
    familiar = models.IntegerField(
        choices=[
            [1, 'Yes'],
            [2, 'No'],
            [3, 'Not Sure'],
        ],
        label='Had you known this project before?'
    )
    knowledge = models.IntegerField(
        choices=[[0, '(No prior knowledge) 0'],
                 [1, "1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7 (Expert prior knowledge)']
                 ],
        widget=widgets.RadioSelectHorizontal, label='How would you assess your knowledge of the topic, prior to the talk?'
    )
    like = models.IntegerField(
        choices=[[0, '(I certainly would not) 0'],
                 [1, "1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7 (I certainly would)']
                 ],
        widget=widgets.RadioSelectHorizontal, label='Would you like to learn more about the project?'
    )
    enjoy = models.IntegerField(
        choices=[[0, '(Not at all) 0'],
                 [1, "1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7 (Very much)']
                 ],
        widget=widgets.RadioSelectHorizontal, label='How much did you enjoy the presentation?'
    )
    clarity = models.IntegerField(
        choices=[[0, '(Not clear at all) 0'],
                 [1, "1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7 (Completely clear)']
                 ],
        widget=widgets.RadioSelectHorizontal, label='How clear was the presentation?'
    )
    connection = models.IntegerField(
        choices=[[0, '(Not at all) 0'],
                 [1, "1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7 (Very well)']
                 ],
        widget=widgets.RadioSelectHorizontal, label='Do you think the speaker could connect well with the audience?'
    )
    easiness = models.IntegerField(
        choices=[[-3, '(way too difficult?) -3'],
                 [-2, "-2"],
                 [-1, "-1"],
                 [0, "0"],
                 [1, "1"],
                 [2, "2"],
                 [3, "3 (way too easy?)"]],
        widget=widgets.RadioSelectHorizontal, label='For you, was the presentation...'
    )
    onoff = models.IntegerField(
        choices=[
            [1, 'Yes'],
            [2, 'No'],
            [3, "I didn't pay attention to this detail"],
        ],
        label='Were the cameras on or off during this meeting?'
    )
    cameras = models.LongStringField(blank=False, label='How did it affect your experience, including your ability to follow the talk?')
    remarks = models.LongStringField(blank=True, label='Any further remarks, reflections on your experience as a Listener or specific suggestions for the Speaker?')
    no_guess = models.BooleanField(blank=False, choices=[[True, 'I would like to guess the results now!'], [False, 'No thanks, I’m done!']],
                                   initial=True,
                                   widget=widgets.RadioSelect,
                                   label='<span style="line-height:1.7;font-size:25px"><font color="#33CC33">Do you want to continue?</font></span>')
    cameras_good = models.LongStringField(blank=True, label='')
    guess1 = models.IntegerField(
        choices=[[1, 'more than 15% higher when cameras are ON'],
                 [2, "5-15% higher when cameras are ON"],
                 [3, "about the same"],
                 [4, "5-15% higher when cameras are OFF"],
                 [5, "more than 15% higher when cameras are OFF"],
                 ],
        widget=widgets.RadioSelect, label='', blank=False
    )
    guess2 = models.IntegerField(
        choices=[[1, 'more than 15% higher when cameras are ON'],
                 [2, "5-15% higher when cameras are ON"],
                 [3, "about the same"],
                 [4, "5-15% higher when cameras are OFF"],
                 [5, "more than 15% higher when cameras are OFF"],
                 ],
        widget=widgets.RadioSelect, label='', blank=False
    )
    guess3 = models.IntegerField(
        choices=[[1, 'more than 15% higher when cameras are ON'],
                 [2, "5-15% higher when cameras are ON"],
                 [3, "about the same"],
                 [4, "5-15% higher when cameras are OFF"],
                 [5, "more than 15% higher when cameras are OFF"],
                 ],
        widget=widgets.RadioSelect, label='', blank=False
    )
    guess4 = models.IntegerField(
        choices=[[1, 'more than 15% higher when cameras are ON'],
                 [2, "5-15% higher when cameras are ON"],
                 [3, "about the same"],
                 [4, "5-15% higher when cameras are OFF"],
                 [5, "more than 15% higher when cameras are OFF"],
                 ],
        widget=widgets.RadioSelect, label='', blank=False
    )
    guess5 = models.IntegerField(
        choices=[[1, 'more than 15% higher when cameras are ON'],
                 [2, "5-15% higher when cameras are ON"],
                 [3, "about the same"],
                 [4, "5-15% higher when cameras are OFF"],
                 [5, "more than 15% higher when cameras are OFF"],
                 ],
        widget=widgets.RadioSelect, label='', blank=False
    )
    guess1_reversed = models.IntegerField(
        choices=[[1, 'more than 15% higher when cameras are OFF'],
                 [2, "5-15% higher when cameras are OFF"],
                 [3, "about the same"],
                 [4, "5-15% higher when cameras are ON"],
                 [5, "more than 15% higher when cameras are ON"],
                 ],
        widget=widgets.RadioSelect, label='', blank=False
    )
    guess2_reversed = models.IntegerField(
        choices=[[1, 'more than 15% higher when cameras are OFF'],
                 [2, "5-15% higher when cameras are OFF"],
                 [3, "about the same"],
                 [4, "5-15% higher when cameras are ON"],
                 [5, "more than 15% higher when cameras are ON"],
                 ],
        widget=widgets.RadioSelect, label='', blank=False
    )
    guess3_reversed = models.IntegerField(
        choices=[[1, 'more than 15% higher when cameras are OFF'],
                 [2, "5-15% higher when cameras are OFF"],
                 [3, "about the same"],
                 [4, "5-15% higher when cameras are ON"],
                 [5, "more than 15% higher when cameras are ON"],
                 ],
        widget=widgets.RadioSelect, label='', blank=False
    )
    guess4_reversed = models.IntegerField(
        choices=[[1, 'more than 15% higher when cameras are OFF'],
                 [2, "5-15% higher when cameras are OFF"],
                 [3, "about the same"],
                 [4, "5-15% higher when cameras are ON"],
                 [5, "more than 15% higher when cameras are ON"],
                 ],
        widget=widgets.RadioSelect, label='', blank=False
    )
    guess5_reversed = models.IntegerField(
        choices=[[1, 'more than 15% higher when cameras are OFF'],
                 [2, "5-15% higher when cameras are OFF"],
                 [3, "about the same"],
                 [4, "5-15% higher when cameras are ON"],
                 [5, "more than 15% higher when cameras are ON"],
                 ],
        widget=widgets.RadioSelect, label='', blank=False
    )