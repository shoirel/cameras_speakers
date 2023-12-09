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
Survey on Overprecision
"""


class Constants(BaseConstants):
    name_in_url = 'intervals'
    players_per_group = None
    num_rounds = 1
    QUESTIONS = ('germans_lower', 'temporary_lower', 'commissioner_lower', 'age_lower', 'allowance_lower', 'paper_lower', 'printers_lower', 'laptops_lower', 'tickets_lower')
    QUESTIONSS = ('germans_higher', 'temporary_higher', 'commissioner_higher', 'age_higher', 'allowance_higher', 'paper_higher', 'printers_higher', 'laptops_higher', 'tickets_higher')
    FEEDBACK = ('feedback', 'no_feedback')
    # OPINIONS = ('germans_comment', 'temporary_comment', 'commissioner_comment', 'age_comment', 'allowance_comment', 'paper_comment', 'printers_comment', 'emails_comment', 'laptops_comment', 'tickets_comment')
    # OPINIONS2 = ('germans_rating', 'temporary_rating', 'commissioner_rating', 'age_rating', 'allowance_rating', 'paper_rating', 'printers_rating', 'emails_rating', 'laptops_rating', 'tickets_rating')


class Subsession(BaseSubsession):
    def creating_session(self):
        session = self.session
        if self.round_number == 1:
            import random as rnd
            players = self.get_players()
            for p in players:
                quests = rnd.sample(
                    list(zip(Constants.QUESTIONS, Constants.QUESTIONSS)),
                    k=len(Constants.QUESTIONS))
                FEEDBACK = rnd.sample(
                Constants.FEEDBACK, k=len(Constants.FEEDBACK))
                p.participant.vars['feedback'] = FEEDBACK
                p.participant.vars['feedback'] = FEEDBACK
                p.FEEDBACK = FEEDBACK[0]
                QUESTIONS, QUESTIONSS = zip(*quests)
                p.participant.vars['qs_order'] = QUESTIONS
                p.participant.vars['qs_order2'] = QUESTIONSS
                # p.participant.vars['qs_order3'] = OPINIONS
                # p.participant.vars['qs_order4'] = OPINIONS2

    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    FEEDBACK = models.StringField()
    # feedback = models.BooleanField(blank=True, label='<span style="line-height:0.1;font-size:0.1px">and</span>')
    # no_feedback = models.BooleanField(blank=True, label='<span style="line-height:0.1;font-size:0.1px">and</span>')
    final = models.LongStringField(blank=True, label='<span style="line-height:1.7;font-size:18px">It is typically found in such studies that<b> much less than 90% of the intervals cover the actual number</b>. Of course, in some cases it can be bad luck, but given that this happens systematically, it is interpreted as what scholars call “overprecision”: many people tend to <b>overestimate the precision of their judgment</b>. This tendency has important consequences for the quality of decision-making in many domains. For example, it might make you underdiversify your investment portfolio ("put all your eggs in the same basket"). <b>If you are managing a project, you may underestimate the likelihood that it ends up taking much more time and money than expected</b>. See e.g., <a href="https://www.researchgate.net/profile/Elizabeth-Tenney/publication/316228342_Overprecision_in_Judgment/links/60abfb7b299bf1031fc843a8/Overprecision-in-Judgment.pdf" target="_blank">Overprecision in Judgment (Moore et al.)</a> to learn more (in particular, see section <em>Ecological Evidence of Overprecision</em> for some examples of real-life consequences of overprecision). For example, you will learn about the advantages and limitations of the kind of study you have just participated in.</span><span></span><span style="line-height:1.7;font-size:18px">Interestingly, many people guess that less than 90% of their intervals will cover the true values, probably intuiting their own overprecision.</span><p></p><span style="line-height:1.7;font-size:18px">If you have any (further) comments on the experiment, please make them below, ideally signing them. You can also contact me directly (e.g.if you want to provide your comments in a conversation -- that would be most helpful).</span><right> <span style="line-height:1.7;font-size:18px">Michal Krawczyk</span></right>')
    germans_lower = models.IntegerField(blank=True,
                             label='<span style="line-height:1.7;font-size:18px">The European Commission has about 32,000 employees. How many of them are German native speakers?</span><span style="line-height:1.7;font-size:18px"><font color =\'green\'>Please answer in <b>absolute numbers</b>, not in terms of percentage of the total number of employees.</font></span><span style="line-height:1.7;font-size:18px"><p></p> I am 90% sure that the number is between</span>',
                             min=0, max=40000)
    germans_higher = models.IntegerField(blank=True, label='<span otree>and</span>', min=0, max=40000)
    temporary_lower = models.IntegerField(blank=True,
                             label='<span style="line-height:1.7;font-size:18px">The European Commission has about 32,000 employees. How many of them are temporary staff? </span><span style="line-height:1.7;font-size:18px"><font color =\'green\'>Please answer in <b>absolute numbers</b>, not in terms of percentage of the total number of employees. </font></span><span style="line-height:1.7;font-size:18px"> <p></p> I am 90% sure that the number is between</span>',
                             min=0, max=40000)
    temporary_higher = models.IntegerField(blank=True, label='<span style="line-height:1.7;font-size:18px">and</span>', min=0, max=40000)
    commissioner_lower = models.IntegerField(blank=True,
                             label='<span style="line-height:1.7;font-size:18px">How many<b> different </b>people ever served as European Commissioners (it counts as one if the same individual was a member of two or more Commissions)?</span><span style="line-height:1.7;font-size:18px"> <p></p> I am 90% sure that the number is between</span>',
                             min=0)
    commissioner_higher = models.IntegerField(blank=True, label='<span style="line-height:1.7;font-size:18px">and</span>', min=0)
    age_lower = models.IntegerField(blank=True,
                             label='<span style="line-height:1.7;font-size:18px">What is she average age of the 27 members of the von der Leyen Commission?</span><span style="line-height:1.7;font-size:18px"> <p></p> I am 90% sure that the number is between</span>',
                             min=18, max = 120)
    age_higher = models.IntegerField(blank=True, label='<span style="line-height:1.7;font-size:18px">and</span>', min=0, max =120)
    allowance_lower = models.IntegerField(blank=True,
                             label='<span style="line-height:1.7;font-size:18px">What was, back in 2016, the monthly “entertainment allowance” of the President of the Commission (in EUR)?</span><span style="line-height:1.7;font-size:18px"> <p></p> I am 90% sure that the number is between</span>',
                             min=0)
    allowance_higher = models.IntegerField(blank=True, label='<span style="line-height:1.7;font-size:18px">and</span>', min=0)
    # cited_lower = models.IntegerField(blank=True,
    #                           label='<span style="line-height:1.7;font-size:18px">Sigmund Freud has been cited about 600 thousand times. What is the number [in thousands] for the most-cited scholar currently affiliated with the Joint Research Centre of the EC? </span><span style="line-height:1.7;font-size:18px"> <p></p> I am 90% sure that the number is between</span>',
    #                           min=0)
    # cited_higher = models.IntegerField(blank=True, label='<span style="line-height:1.7;font-size:18px">and</span>', min=0)
    paper_lower = models.IntegerField(blank=True,
                              label='<span style="line-height:1.7;font-size:18px">The EC used about 300 tonnes of office paper in 2020. How many tonnes did it use in 2019? </span><span style="line-height:1.7;font-size:18px"> <p></p> I am 90% sure that the number is between</span>',
                              min=0)
    paper_higher = models.IntegerField(blank=True, label='<span style="line-height:1.7;font-size:18px">and</span>', min=0)
    printers_lower = models.IntegerField(blank=True,
                              label='<span style="line-height:1.7;font-size:18px">The EC had about 7360 individual printers in 2018. How many did it have in 2019? </span><span style="line-height:1.7;font-size:18px"> <p></p> I am 90% sure that the number is between</span>',
                              min=0)
    printers_higher = models.IntegerField(blank=True, label='<span style="line-height:1.7;font-size:18px">and</span>', min=0)
    # driving_lower = models.IntegerField(blank=True,
    #                           label='<span style="line-height:1.7;font-size:18px">The 120 EC vehicles based in Ispra drove about 150 thousand km in 2020. How many <b>thousand</b> km did the 130 Brussels-based vehicles drive? </span><span style="line-height:1.7;font-size:18px"> <p></p> I am 90% sure that the number is between</span>',
    #                           min=0)
    # driving_higher = models.IntegerField(blank=True, label='<span style="line-height:1.7;font-size:18px">and</span>', min=0)
    # emissions_lower = models.IntegerField(blank=True,
    #                           label='<span style="line-height:1.7;font-size:18px">EC staff commuting caused some 5400 tonnes of CO2 being emitted in 2020. How much (in tonnes) did <b>the missions</b> cause in the same year? </span><span style="line-height:1.7;font-size:18px"> <p></p> I am 90% sure that the number is between</span>',
    #                           min=0)
    # emissions_higher = models.IntegerField(blank=True, label='<span style="line-height:1.7;font-size:18px">and</span>', min=0)
    emails_lower = models.IntegerField(blank=True,
                              label='<span style="line-height:1.7;font-size:18px">How many e-mails does a typical EC employee send (from his or her corporate account) on a typical working day? </span><span style="line-height:1.7;font-size:18px"><p></p> I am 90% sure that the <b>number</b> is between</span>',
                              min=0)
    emails_higher = models.IntegerField(blank=True, label='<span style="line-height:1.7;font-size:18px">and</span>', min=0)
    laptops_lower = models.IntegerField(blank=True,
                              label='<span style="line-height:1.7;font-size:18px">How many laptops does the EC purchase yearly?</span><span style="line-height:1.7;font-size:18px"> <p></p> I am 90% sure that the number is between</span>',
                              min=0)
    laptops_higher = models.IntegerField(blank=True, label='<span style="line-height:1.7;font-size:18px">and</span>', min=0)
    tickets_lower = models.IntegerField(blank=True,
                              label='<span style="line-height:1.7;font-size:18px">What is the average <b>daily</b> number of tickets (requests) that the IT helpdesk of the EC receives?</span><span style="line-height:1.7;font-size:18px"> <p></p> I am 90% sure that the number is between</span>',
                              min=0)
    tickets_higher = models.IntegerField(blank=True, label='<span style="line-height:1.7;font-size:18px">and</span>', min=0)
    skip_all = models.BooleanField(blank=True, choices=[[True, 'Yes, next question, please!'], [False,
                                                                                                'No more questions, please, just tell me what it’s about!']],
                                   initial=True, label='<p></p><span style="line-height:1.7;font-size:30px"></span>Do you want to continue?')
    assumed = models.IntegerField(label = '', max=10, min=0)


    # germans_comment = models.LongStringField(blank=True,
    #                             label='<span style="line-height:1.7;font-size:12px">If this question is really cool/ really boring/ too easy/ too difficult/ imprecise or unclear/ weird/ potentially offensive/ you have other comments, please let us know</span>')
    # temporary_comment = models.LongStringField(blank=True,
    #                             label='<span style="line-height:1.7;font-size:12px">If this question is really cool/ really boring/ too easy/ too difficult/ imprecise or unclear/ weird/ potentially offensive/ you have other comments, please let us know</span>')
    # commissioner_comment = models.LongStringField(blank=True,
    #                             label='<span style="line-height:1.7;font-size:12px">If this question is really cool/ really boring/ too easy/ too difficult/ imprecise or unclear/ weird/ potentially offensive/ you have other comments, please let us know</span>')
    # age_comment = models.LongStringField(blank=True,
    #                             label='<span style="line-height:1.7;font-size:12px">If this question is really cool/ really boring/ too easy/ too difficult/ imprecise or unclear/ weird/ potentially offensive/ you have other comments, please let us know</span>')
    # allowance_comment = models.LongStringField(blank=True,
    #                             label='<span style="line-height:1.7;font-size:12px">If this question is really cool/ really boring/ too easy/ too difficult/ imprecise or unclear/ weird/ potentially offensive/ you have other comments, please let us know</span>')
    # cited_comment = models.LongStringField(blank=True,
    #                             label='<span style="line-height:1.7;font-size:12px">If this question is really cool/ really boring/ too easy/ too difficult/ imprecise or unclear/ weird/ potentially offensive/ you have other comments, please let us know</span>')
    # paper_comment = models.LongStringField(blank=True,
    #                             label='<span style="line-height:1.7;font-size:12px">If this question is really cool/ really boring/ too easy/ too difficult/ imprecise or unclear/ weird/ potentially offensive/ you have other comments, please let us know</span>')
    # printers_comment = models.LongStringField(blank=True,
    #                             label='<span style="line-height:1.7;font-size:12px">If this question is really cool/ really boring/ too easy/ too difficult/ imprecise or unclear/ weird/ potentially offensive/ you have other comments, please let us know</span>')
    # driving_comment = models.LongStringField(blank=True,
    #                             label='<span style="line-height:1.7;font-size:12px">If this question is really cool/ really boring/ too easy/ too difficult/ imprecise or unclear/ weird/ potentially offensive/ you have other comments, please let us know</span>')
    # emissions_comment = models.LongStringField(blank=True,
    #                              label='<span style="line-height:1.7;font-size:12px">If this question is really cool/ really boring/ too easy/ too difficult/ imprecise or unclear/ weird/ potentially offensive/ you have other comments, please let us know</span>')
    # emails_comment = models.LongStringField(blank=True,
    #                              label='<span style="line-height:1.7;font-size:12px">If this question is really cool/ really boring/ too easy/ too difficult/ imprecise or unclear/ weird/ potentially offensive/ you have other comments, please let us know</span>')
    # laptops_comment = models.LongStringField(blank=True,
    #                              label='<span style="line-height:1.7;font-size:12px">If this question is really cool/ really boring/ too easy/ too difficult/ imprecise or unclear/ weird/ potentially offensive/ you have other comments, please let us know</span>')
    # tickets_comment = models.LongStringField(blank=True,
    #                              label='<span style="line-height:1.7;font-size:12px">If this question is really cool/ really boring/ too easy/ too difficult/ imprecise or unclear/ weird/ potentially offensive/ you have other comments, please let us know</span>')
    # germans_rating = models.IntegerField(
    #     label='<span> </span><span style="line-height:1.7;font-size:18px">On a scale from 0 to 5, how do you like this question?</span>',
    #     blank=False,
    #     choices=[
    #         [0, '0'],
    #         [1, '1'],
    #         [2, '2'],
    #         [3, '3'],
    #         [4, '4'],
    #         [5, '5'],
    #     ],
    #     widget=widgets.RadioSelectHorizontal
    # )
    # temporary_rating = models.IntegerField(
    #     label='<span> </span><span style="line-height:1.7;font-size:18px">On a scale from 0 to 5, how do you like this question?</span>',
    #     blank=False,
    #     choices=[
    #         [0, '0'],
    #         [1, '1'],
    #         [2, '2'],
    #         [3, '3'],
    #         [4, '4'],
    #         [5, '5'],
    #     ],
    #     widget=widgets.RadioSelectHorizontal
    # )
    # commissioner_rating = models.IntegerField(
    #     label='<span> </span><span style="line-height:1.7;font-size:18px">On a scale from 0 to 5, how do you like this question?</span>',
    #     blank=False,
    #     choices=[
    #         [0, '0'],
    #         [1, '1'],
    #         [2, '2'],
    #         [3, '3'],
    #         [4, '4'],
    #         [5, '5'],
    #     ],
    #     widget=widgets.RadioSelectHorizontal
    # )
    # age_rating = models.IntegerField(
    #     label='<span> </span><span style="line-height:1.7;font-size:18px">On a scale from 0 to 5, how do you like this question?</span>',
    #     blank=False,
    #     choices=[
    #         [0, '0'],
    #         [1, '1'],
    #         [2, '2'],
    #         [3, '3'],
    #         [4, '4'],
    #         [5, '5'],
    #     ],
    #     widget=widgets.RadioSelectHorizontal
    # )
    # allowance_rating = models.IntegerField(
    #     label='<span> </span><span style="line-height:1.7;font-size:18px">On a scale from 0 to 5, how do you like this question?</span>',
    #     blank=False,
    #     choices=[
    #         [0, '0'],
    #         [1, '1'],
    #         [2, '2'],
    #         [3, '3'],
    #         [4, '4'],
    #         [5, '5'],
    #     ],
    #     widget=widgets.RadioSelectHorizontal
    # )
    # cited_rating = models.IntegerField(
    #     label='<span> </span><span style="line-height:1.7;font-size:18px">On a scale from 0 to 5, how do you like this question?</span>',
    #     blank=False,
    #     choices=[
    #         [0, '0'],
    #         [1, '1'],
    #         [2, '2'],
    #         [3, '3'],
    #         [4, '4'],
    #         [5, '5'],
    #     ],
    #     widget=widgets.RadioSelectHorizontal
    # )
    # paper_rating = models.IntegerField(
    #     label='<span> </span><span style="line-height:1.7;font-size:18px">On a scale from 0 to 5, how do you like this question?</span>',
    #     blank=False,
    #     choices=[
    #         [0, '0'],
    #         [1, '1'],
    #         [2, '2'],
    #         [3, '3'],
    #         [4, '4'],
    #         [5, '5'],
    #     ],
    #     widget=widgets.RadioSelectHorizontal
    # )
    # printers_rating = models.IntegerField(
    #     label='<span> </span><span style="line-height:1.7;font-size:18px">On a scale from 0 to 5, how do you like this question?</span>',
    #     blank=False,
    #     choices=[
    #         [0, '0'],
    #         [1, '1'],
    #         [2, '2'],
    #         [3, '3'],
    #         [4, '4'],
    #         [5, '5'],
    #     ],
    #     widget=widgets.RadioSelectHorizontal
    # )
    # driving_rating = models.IntegerField(
    #     label='<span> </span><span style="line-height:1.7;font-size:18px">On a scale from 0 to 5, how do you like this question?</span>',
    #     blank=False,
    #     choices=[
    #         [0, '0'],
    #         [1, '1'],
    #         [2, '2'],
    #         [3, '3'],
    #         [4, '4'],
    #         [5, '5'],
    #     ],
    #     widget=widgets.RadioSelectHorizontal
    # )
    # emissions_rating = models.IntegerField(
    #     label='<span> </span><span style="line-height:1.7;font-size:18px">On a scale from 0 to 5, how do you like this question?</span>',
    #     blank=False,
    #     choices=[
    #         [0, '0'],
    #         [1, '1'],
    #         [2, '2'],
    #         [3, '3'],
    #         [4, '4'],
    #         [5, '5'],
    #     ],
    #     widget=widgets.RadioSelectHorizontal
    # )
    # emails_rating = models.IntegerField(
    #     label='<span> </span><span style="line-height:1.7;font-size:18px">On a scale from 0 to 5, how do you like this question?</span>',
    #     blank=False,
    #     choices=[
    #         [0, '0'],
    #         [1, '1'],
    #         [2, '2'],
    #         [3, '3'],
    #         [4, '4'],
    #         [5, '5'],
    #     ],
    #     widget=widgets.RadioSelectHorizontal
    # )
    # laptops_rating = models.IntegerField(
    #     label='<span> </span><span style="line-height:1.7;font-size:18px">On a scale from 0 to 5, how do you like this question?</span>',
    #     blank=False,
    #     choices=[
    #         [0, '0'],
    #         [1, '1'],
    #         [2, '2'],
    #         [3, '3'],
    #         [4, '4'],
    #         [5, '5'],
    #     ],
    #     widget=widgets.RadioSelectHorizontal
    # )
    # tickets_rating = models.IntegerField(
    #     label='<span> </span><span style="line-height:1.7;font-size:18px">On a scale from 0 to 5, how do you like this question?</span>',
    #     blank=False,
    #     choices=[
    #         [0, '0'],
    #         [1, '1'],
    #         [2, '2'],
    #         [3, '3'],
    #         [4, '4'],
    #         [5, '5'],
    #     ],
    #     widget=widgets.RadioSelectHorizontal
    # )