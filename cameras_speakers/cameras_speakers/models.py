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
    name_in_url = 'cameras_speakers'
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
    rec_kept = models.IntegerField(blank=False,
        choices=[
            [1, 'Yes, I am OK with it'],
            [2, 'No, I want the recording to be deleted'],
            [3, 'I don’t know yet, please send me the recording before I decide'],
        ],
        label='<p><font color="#009933">Do you agree that the recording of your talk is kept, possibly to be shared '
              'within the Commission'
              ' to promote your project? </font>It also means taking part in the competition '
              'for the best talk. If you give consent after each of your two performances, they will have an'
              ' independent chance in the competition.</p> Please note that if you choose “Yes”, '
              'we will also send you the recording.'
    )
    reflections = models.LongStringField(label='', blank=True)
    satisfied = models.IntegerField(blank=False,
        choices=[[1, '(Not at all satisfied) 1'],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7 (Fully satisfied)']
                 ],
        widget=widgets.RadioSelectHorizontal, label='How satisfied are you with your talk?'
    )
    like = models.IntegerField(
        choices=[[0, '(They certainly would not) 0'],
                 [1, "1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7 (They certainly would)']
                 ],
        widget=widgets.RadioSelectHorizontal, label='Would they like to learn more about your project?', blank=True
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
        widget=widgets.RadioSelectHorizontal, label='How much did they enjoy your presentation?', blank=True
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
        widget=widgets.RadioSelectHorizontal, label='How clear was your presentation?', blank=True
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
        widget=widgets.RadioSelectHorizontal, label='Did they think you could connect well with the audience?',
        blank=True
    )
    easiness = models.IntegerField(
        choices=[[-3, '(way too difficult?) -3'],
                 [-2, "-2"],
                 [-1, "-1"],
                 [0, "0"],
                 [1, "1"],
                 [2, "2"],
                 [3, "3 (way too easy?)"]],
        widget=widgets.RadioSelectHorizontal, label='For them, was your presentation...', blank=True
    )
    assess1 = models.IntegerField(blank=False,
        choices=[[0,"0"],
                 [1,"1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7']
                 ],
        widget=widgets.RadioSelectHorizontal, label='How would you assess this summary? '
                                                    'Please choose on a <b>scale from 0</b> ("This text does not summarise '
                                                    'my project at all") <b>to 7</b> ("This text is an excellent summary of'
                                                    'my project").'
                                                    'Please note that this assessment <b>WILL NOT</b> be sent to the '
                                                    'relevant Listener.'
    )
    assess2 = models.IntegerField(blank=False,
        choices=[[0,"0"],
                 [1,"1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7']
                 ],
        widget=widgets.RadioSelectHorizontal, label='How would you assess this summary? '
                                                    'Please choose on a <b>scale from 0</b> ("This text does not summarise '
                                                    'my project at all") <b>to 7</b> ("This text is an excellent summary of'
                                                    'my project").'
                                                    'Please note that this assessment <b>WILL NOT</b> be sent to the '
                                                    'relevant Listener.'
    )
    assess3 = models.IntegerField(blank=False,
        choices=[[0,"0"],
                 [1,"1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7']
                 ],
        widget=widgets.RadioSelectHorizontal, label='How would you assess this summary? '
                                                    'Please choose on a <b>scale from 0</b> ("This text does not summarise '
                                                    'my project at all") <b>to 7</b> ("This text is an excellent summary of'
                                                    'my project").'
                                                    'Please note that this assessment <b>WILL NOT</b> be sent to the '
                                                    'relevant Listener.'
    )
    assess4 = models.IntegerField(blank=False,
        choices=[[0,"0"],
                 [1,"1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7']
                 ],
        widget=widgets.RadioSelectHorizontal, label='How would you assess this summary? '
                                                    'Please choose on a <b>scale from 0</b> ("This text does not summarise '
                                                    'my project at all") <b>to 7</b> ("This text is an excellent summary of'
                                                    'my project").'
                                                    'Please note that this assessment <b>WILL NOT</b> be sent to the '
                                                    'relevant Listener.'
    )
    assess5 = models.IntegerField(blank=False,
        choices=[[0,"0"],
                 [1,"1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7']
                 ],
        widget=widgets.RadioSelectHorizontal, label='How would you assess this summary? '
                                                    'Please choose on a <b>scale from 0</b> ("This text does not summarise '
                                                    'my project at all") <b>to 7</b> ("This text is an excellent summary of'
                                                    'my project").'
                                                    'Please note that this assessment <b>WILL NOT</b> be sent to the '
                                                    'relevant Listener.'
    )
    assess6 = models.IntegerField(blank=False,
        choices=[[0,"0"],
                 [1,"1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7']
                 ],
        widget=widgets.RadioSelectHorizontal, label='How would you assess this summary? '
                                                    'Please choose on a <b>scale from 0</b> ("This text does not summarise '
                                                    'my project at all") <b>to 7</b> ("This text is an excellent summary of'
                                                    'my project").'
                                                    'Please note that this assessment <b>WILL NOT</b> be sent to the '
                                                    'relevant Listener.'
    )
    assess7 = models.IntegerField(blank=False,
        choices=[[0,"0"],
                 [1,"1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7']
                 ],
        widget=widgets.RadioSelectHorizontal, label='How would you assess this summary? '
                                                    'Please choose on a <b>scale from 0</b> ("This text does not summarise '
                                                    'my project at all") <b>to 7</b> ("This text is an excellent summary of'
                                                    'my project").'
                                                    'Please note that this assessment <b>WILL NOT</b> be sent to the '
                                                    'relevant Listener.'
    )
    assess1_txt = models.LongStringField(blank=True, label='What aspects of '
                                                          'this summary do you particularly like or dislike? Any other'
                                                          ' thoughts about it? Please note that this assessment <b>WILL</b> '
                                                          'be sent to the relevant Listener.')
    assess2_txt = models.LongStringField(blank=True, label='What aspects of '
                                                          'this summary do you particularly like or dislike? Any other'
                                                          ' thoughts about it? Please note that this assessment <b>WILL</b> '
                                                          'be sent to the relevant Listener.')
    assess3_txt = models.LongStringField(blank=True, label='What aspects of '
                                                          'this summary do you particularly like or dislike? Any other'
                                                          ' thoughts about it? Please note that this assessment <b>WILL</b> '
                                                          'be sent to the relevant Listener.')
    assess4_txt = models.LongStringField(blank=True, label='What aspects of '
                                                          'this summary do you particularly like or dislike? Any other'
                                                          ' thoughts about it? Please note that this assessment <b>WILL</b> '
                                                          'be sent to the relevant Listener.')
    assess5_txt = models.LongStringField(blank=True, label='What aspects of '
                                                          'this summary do you particularly like or dislike? Any other'
                                                          ' thoughts about it? Please note that this assessment <b>WILL</b> '
                                                          'be sent to the relevant Listener.')
    assess6_txt = models.LongStringField(blank=True, label='What aspects of '
                                                          'this summary do you particularly like or dislike? Any other'
                                                          ' thoughts about it? Please note that this assessment <b>WILL</b> '
                                                          'be sent to the relevant Listener.')
    assess7_txt = models.LongStringField(blank=True, label='What aspects of '
                                                          'this summary do you particularly like or dislike? Any other'
                                                          ' thoughts about it? Please note that this assessment <b>WILL</b> '
                                                          'be sent to the relevant Listener.')
    # fake = models.IntegerField(
    #     choices=[[1, 'Summary 1'],
    #              [2, 'Summary 2'],
    #              [3, 'Summary 3'],
    #              [4, 'Summary 4'],
    #              [5, 'Summary 5'],
    #              [6, 'Summary 6'],
    #              [7, 'Summary 7']
    #              ],
    #     widget=widgets.RadioSelectHorizontal, label=''
    # )
    # sure = models.IntegerField(
    #     choices=[[0, '0 (It’s a random guess)'],
    #              [1, '1'],
    #              [2, '2'],
    #              [3, '3'],
    #              [4, '4'],
    #              [5, '5'],
    #              [6, '6'],
    #              [7, '7 (I am 100% sure)']
    #              ],
    #     widget=widgets.RadioSelectHorizontal, label='How sure are you of your answer?'
    # )
    gpt = models.IntegerField(blank=True,
        choices=[[0, '(Definitely not) 0'],
                 [1, "1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7 (Definitely yes)']
                 ],
        widget=widgets.RadioSelectHorizontal, label='Do you think this summary was written by Chat GPT?'
    )
    gpt2 = models.IntegerField(blank=True,
        choices=[[0, '(Definitely not) 0'],
                 [1, "1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7 (Definitely yes)']
                 ],
        widget=widgets.RadioSelectHorizontal, label='Do you think this summary was written by Chat GPT?'
    )
    gpt3 = models.IntegerField(blank=True,
        choices=[[0, '(Definitely not) 0'],
                 [1, "1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7 (Definitely yes)']
                 ],
        widget=widgets.RadioSelectHorizontal, label='Do you think this summary was written by Chat GPT?'
    )
    gpt4 = models.IntegerField(blank=True,
        choices=[[0, '(Definitely not) 0'],
                 [1, "1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7 (Definitely yes)']
                 ],
        widget=widgets.RadioSelectHorizontal, label='Do you think this summary was written by Chat GPT?'
    )
    gpt5 = models.IntegerField(blank=True,
        choices=[[0, '(Definitely not) 0'],
                 [1, "1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7 (Definitely yes)']
                 ],
        widget=widgets.RadioSelectHorizontal, label='Do you think this summary was written by Chat GPT?'
    )
    gpt6 = models.IntegerField(blank=True,
        choices=[[0, '(Definitely not) 0'],
                 [1, "1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7 (Definitely yes)']
                 ],
        widget=widgets.RadioSelectHorizontal, label='Do you think this summary was written by Chat GPT?'
    )
    gpt7 = models.IntegerField(blank=True,
        choices=[[0, '(Definitely not) 0'],
                 [1, "1"],
                 [2, "2"],
                 [3, "3"],
                 [4, "4"],
                 [5, "5"],
                 [6, "6"],
                 [7, '7 (Definitely yes)']
                 ],
        widget=widgets.RadioSelectHorizontal, label='Do you think this summary was written by Chat GPT?'
    )
    cameras = models.LongStringField(blank=False,label='As you have noticed, cameras were on during one of your talks'
                                                       ' and off during the other talk. How do you think this '
                                                       'affected your performance and everyone’s experience?')
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
        widget=widgets.RadioSelect, label=''
    )
    guess2 = models.IntegerField(
        choices=[[1, 'more than 15% higher when cameras are ON'],
                 [2, "5-15% higher when cameras are ON"],
                 [3, "about the same"],
                 [4, "5-15% higher when cameras are OFF"],
                 [5, "more than 15% higher when cameras are OFF"],
                 ],
        widget=widgets.RadioSelect, label=''
    )
    guess3 = models.IntegerField(
        choices=[[1, 'more than 15% higher when cameras are ON'],
                 [2, "5-15% higher when cameras are ON"],
                 [3, "about the same"],
                 [4, "5-15% higher when cameras are OFF"],
                 [5, "more than 15% higher when cameras are OFF"],
                 ],
        widget=widgets.RadioSelect, label=''
    )
    guess4 = models.IntegerField(
        choices=[[1, 'more than 15% higher when cameras are ON'],
                 [2, "5-15% higher when cameras are ON"],
                 [3, "about the same"],
                 [4, "5-15% higher when cameras are OFF"],
                 [5, "more than 15% higher when cameras are OFF"],
                 ],
        widget=widgets.RadioSelect, label=''
    )
    guess5 = models.IntegerField(
        choices=[[1, 'more than 15% higher when cameras are ON'],
                 [2, "5-15% higher when cameras are ON"],
                 [3, "about the same"],
                 [4, "5-15% higher when cameras are OFF"],
                 [5, "more than 15% higher when cameras are OFF"],
                 ],
        widget=widgets.RadioSelect, label=''
    )
    guess1_reversed = models.IntegerField(
        choices=[[1, 'more than 15% higher when cameras are OFF'],
                 [2, "5-15% higher when cameras are OFF"],
                 [3, "about the same"],
                 [4, "5-15% higher when cameras are ON"],
                 [5, "more than 15% higher when cameras are ON"],
                 ],
        widget=widgets.RadioSelect, label=''
    )
    guess2_reversed = models.IntegerField(
        choices=[[1, 'more than 15% higher when cameras are OFF'],
                 [2, "5-15% higher when cameras are OFF"],
                 [3, "about the same"],
                 [4, "5-15% higher when cameras are ON"],
                 [5, "more than 15% higher when cameras are ON"],
                 ],
        widget=widgets.RadioSelect, label=''
    )
    guess3_reversed = models.IntegerField(
        choices=[[1, 'more than 15% higher when cameras are OFF'],
                 [2, "5-15% higher when cameras are OFF"],
                 [3, "about the same"],
                 [4, "5-15% higher when cameras are ON"],
                 [5, "more than 15% higher when cameras are ON"],
                 ],
        widget=widgets.RadioSelect, label=''
    )
    guess4_reversed = models.IntegerField(
        choices=[[1, 'more than 15% higher when cameras are OFF'],
                 [2, "5-15% higher when cameras are OFF"],
                 [3, "about the same"],
                 [4, "5-15% higher when cameras are ON"],
                 [5, "more than 15% higher when cameras are ON"],
                 ],
        widget=widgets.RadioSelect, label=''
    )
    guess5_reversed = models.IntegerField(
        choices=[[1, 'more than 15% higher when cameras are OFF'],
                 [2, "5-15% higher when cameras are OFF"],
                 [3, "about the same"],
                 [4, "5-15% higher when cameras are ON"],
                 [5, "more than 15% higher when cameras are ON"],
                 ],
        widget=widgets.RadioSelect, label=''
    )
