from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Welcome(Page):
    form_model = 'player'


class Q1(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        set1 = ['emails_lower', 'emails_higher', 'skip_all']
        return set1

    def error_message(self, values):
        participant = self.player.participant
        germans_lower = participant.vars['qs_order'][0]
        germans_higher = participant.vars['qs_order2'][0]
        print('values is', values)
        try:
            if values['emails_lower'] >= values['emails_higher']:
                return "When you claim that the number we asked about is between A and B, please make sure that your " \
                       "B is larger than A. "
        except:
            pass


class Q1feedback(Page):
    form_model = 'player'

    def is_displayed(self):
        q1 = self.player.emails_lower
        q2 = self.player.emails_higher

        if q1 is not None and q2 is not None and self.player.participant.vars['feedback'][0] == "feedback":
            return True

    def vars_for_template(self):
        participant = self.player.participant
        q1 = self.player.emails_lower
        q2 = self.player.emails_higher
        correct = 53

        return dict(
            q1=q1,
            q2=q2,
            correct=correct,
        )


class Q2(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        set1 = [participant.vars['qs_order'][0], participant.vars['qs_order2'][0],
                'skip_all']
        return set1

    def is_displayed(self):
        if self.player.skip_all == True:
            return True

    def error_message(self, values):
        participant = self.player.participant
        print('values is', values)
        try:
            if values[participant.vars['qs_order'][0]] >= values[participant.vars['qs_order2'][0]]:
                return "When you claim that the number we asked about is between A and B, please make sure that your " \
                       "B is larger than A. "
        except:
            pass


class Q2feedback(Page):
    form_model = 'player'

    def is_displayed(self):
        participant = self.player.participant
        if participant.vars['qs_order'][0] == "germans_lower":
            q3 = self.player.germans_lower
        elif participant.vars['qs_order'][0] == "temporary_lower":
            q3 = self.player.temporary_lower
        elif participant.vars['qs_order'][0] == "commissioner_lower":
            q3 = self.player.commissioner_lower
        elif participant.vars['qs_order'][0] == "age_lower":
            q3 = self.player.age_lower
        elif participant.vars['qs_order'][0] == "allowance_lower":
            q3 = self.player.allowance_lower
        elif participant.vars['qs_order'][0] == "paper_lower":
            q3 = self.player.paper_lower
        elif participant.vars['qs_order'][0] == "printers_lower":
            q3 = self.player.printers_lower
        elif participant.vars['qs_order'][0] == "laptops_lower":
            q3 = self.player.laptops_lower
        else:
            # participant.vars['qs_order'][0] == "tickets_lower"
            q3 = self.player.tickets_lower

        if participant.vars['qs_order2'][0] == "germans_higher":
            q4 = self.player.germans_higher
        elif participant.vars['qs_order2'][0] == "temporary_higher":
            q4 = self.player.temporary_higher
        elif participant.vars['qs_order2'][0] == "commissioner_higher":
            q4 = self.player.commissioner_higher
        elif participant.vars['qs_order2'][0] == "age_higher":
            q4 = self.player.age_higher
        elif participant.vars['qs_order2'][0] == "allowance_higher":
            q4 = self.player.allowance_higher
        elif participant.vars['qs_order2'][0] == "paper_higher":
            q4 = self.player.paper_higher
        elif participant.vars['qs_order2'][0] == "printers_higher":
            q4 = self.player.printers_higher
        elif participant.vars['qs_order2'][0] == "laptops_higher":
            q4 = self.player.laptops_higher
        else:
            # participant.vars['qs_order2'][0] == "tickets_higher":
            q4 = self.player.tickets_higher

        if q3 is not None and q4 is not None and self.player.participant.vars['feedback'][0] == "feedback":
            return True

    def vars_for_template(self):
        participant = self.player.participant
        if participant.vars['qs_order'][0] == "germans_lower":
            q3 = self.player.germans_lower
            correct = 2700
        elif participant.vars['qs_order'][0] == "temporary_lower":
            q3 = self.player.temporary_lower
            correct = 2340
        elif participant.vars['qs_order'][0] == "commissioner_lower":
            q3 = self.player.commissioner_lower
            correct = 233
        elif participant.vars['qs_order'][0] == "age_lower":
            q3 = self.player.age_lower
            correct = 59
        elif participant.vars['qs_order'][0] == "allowance_lower":
            q3 = self.player.allowance_lower
            correct = 1418
        elif participant.vars['qs_order'][0] == "paper_lower":
            q3 = self.player.paper_lower
            correct = 710
        elif participant.vars['qs_order'][0] == "printers_lower":
            q3 = self.player.printers_lower
            correct = 3503
        elif participant.vars['qs_order'][0] == "laptops_lower":
            q3 = self.player.laptops_lower
            correct = 9000
        else:
            # participant.vars['qs_order'][0] == "tickets_lower"
            q3 = self.player.tickets_lower
            correct = 2250

        if participant.vars['qs_order2'][0] == "germans_higher":
            q4 = self.player.germans_higher
        elif participant.vars['qs_order2'][0] == "temporary_higher":
            q4 = self.player.temporary_higher
        elif participant.vars['qs_order2'][0] == "commissioner_higher":
            q4 = self.player.commissioner_higher
        elif participant.vars['qs_order2'][0] == "age_higher":
            q4 = self.player.age_higher
        elif participant.vars['qs_order2'][0] == "allowance_higher":
            q4 = self.player.allowance_higher
        elif participant.vars['qs_order2'][0] == "paper_higher":
            q4 = self.player.paper_higher
        elif participant.vars['qs_order2'][0] == "printers_higher":
            q4 = self.player.printers_higher
        elif participant.vars['qs_order2'][0] == "laptops_higher":
            q4 = self.player.laptops_higher
        else:
            # participant.vars['qs_order2'][0] == "tickets_higher":
            q4 = self.player.tickets_higher

        question1 = self.player.emails_lower
        question2 = self.player.emails_higher
        question3 = self.player.temporary_lower
        question4 = self.player.temporary_higher
        question5 = self.player.commissioner_lower
        question6 = self.player.commissioner_higher
        question7 = self.player.age_lower
        question8 = self.player.age_higher
        question9 = self.player.allowance_lower
        question10 = self.player.allowance_higher
        question11 = self.player.paper_lower
        question12 = self.player.paper_higher
        question13 = self.player.printers_lower
        question14 = self.player.printers_higher
        question15 = self.player.laptops_lower
        question16 = self.player.laptops_higher
        question17 = self.player.tickets_lower
        question18 = self.player.tickets_higher
        question19 = self.player.germans_lower
        question20 = self.player.germans_higher

        if question1 == None:
            question1 = "(skipped)"
        if question2 == None:
            question2 = "(skipped)"
        if question3 == None:
            question3 = "(skipped)"
        if question4 == None:
            question4 = "(skipped)"
        if question5 == None:
            question5 = "(skipped)"
        if question6 == None:
            question6 = "(skipped)"
        if question7 == None:
            question7 = "(skipped)"
        if question8 == None:
            question8 = "(skipped)"
        if question9 == None:
            question9 = "(skipped)"
        if question10 == None:
            question10 = "(skipped)"
        if question11 == None:
            question11 = "(skipped)"
        if question12 == None:
            question12 = "(skipped)"
        if question13 == None:
            question13 = "(skipped)"
        if question14 == None:
            question14 = "(skipped)"
        if question15 == None:
            question15 = "(skipped)"
        if question16 == None:
            question16 = "(skipped)"
        if question17 == None:
            question17 = "(skipped)"
        if question18 == None:
            question18 = "(skipped)"
        if question19 == None:
            question19 = "(skipped)"
        if question20 == None:
            question20 = "(skipped)"

        down = [question1, question3, question5, question7, question9, question11, question13, question15, question17,
                question19]
        up = [question2, question4, question6, question8, question10, question12, question14, question16, question18,
              question20]

        correct_answers = [53, 2700, 2340, 233, 59, 1418, 710, 3503, 9000, 2250]
        CORRECT = 0
        for i in range(0, len(correct_answers)):
            try:
                if down[i] <= correct_answers[i] <= up[i]:
                    CORRECT += 1
            except:
                continue

        ANSWERED = 0
        for i in range(0, len(correct_answers)):
            try:
                if down[i] >= 0 and up[i] >= 0:
                    ANSWERED += 1
                elif down[i] >= 0 and up[i] == "(skipped)":
                    ANSWERED += 0
                elif down[i] == "(skipped)" and up[i] >= 0:
                    ANSWERED += 0
                else:
                    ANSWERED += 0
            except:
                continue

        CORRECT = round(CORRECT, 1)
        CORRECT_P = round(ANSWERED * 0.9, 1)
        try:
            PERCENT = round(100 * CORRECT / ANSWERED, 1)
        except:
            PERCENT = 0

        return dict(
            CORRECT=CORRECT,
            CORRECT_P=CORRECT_P,
            ANSWERED=ANSWERED,
            PERCENT=PERCENT,
            q3=q3,
            q4=q4,
            correct=correct,
        )


class Q3(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        set2 = [participant.vars['qs_order'][1], participant.vars['qs_order2'][1],
                'skip_all']
        return set2

    def is_displayed(self):
        if self.player.skip_all == True:
            return True

    def error_message(self, values):
        participant = self.player.participant
        print('values is', values)
        try:
            if values[participant.vars['qs_order'][1]] >= values[participant.vars['qs_order2'][1]]:
                return "When you claim that the number we asked about is between A and B, please make sure that your " \
                       "B is larger than A. "
        except:
            pass


class Q3feedback(Page):
    form_model = 'player'

    def is_displayed(self):
        participant = self.player.participant
        if participant.vars['qs_order'][1] == "germans_lower":
            q5 = self.player.germans_lower
        elif participant.vars['qs_order'][1] == "temporary_lower":
            q5 = self.player.temporary_lower
        elif participant.vars['qs_order'][1] == "commissioner_lower":
            q5 = self.player.commissioner_lower
        elif participant.vars['qs_order'][1] == "age_lower":
            q5 = self.player.age_lower
        elif participant.vars['qs_order'][1] == "allowance_lower":
            q5 = self.player.allowance_lower
        elif participant.vars['qs_order'][1] == "paper_lower":
            q5 = self.player.paper_lower
        elif participant.vars['qs_order'][1] == "printers_lower":
            q5 = self.player.printers_lower
        elif participant.vars['qs_order'][1] == "laptops_lower":
            q5 = self.player.laptops_lower
        else:
            # participant.vars['qs_order'][1] == "tickets_lower"
            q5 = self.player.tickets_lower

        if participant.vars['qs_order2'][1] == "germans_higher":
            q6 = self.player.germans_higher
        elif participant.vars['qs_order2'][1] == "temporary_higher":
            q6 = self.player.temporary_higher
        elif participant.vars['qs_order2'][1] == "commissioner_higher":
            q6 = self.player.commissioner_higher
        elif participant.vars['qs_order2'][1] == "age_higher":
            q6 = self.player.age_higher
        elif participant.vars['qs_order2'][1] == "allowance_higher":
            q6 = self.player.allowance_higher
        elif participant.vars['qs_order2'][1] == "paper_higher":
            q6 = self.player.paper_higher
        elif participant.vars['qs_order2'][1] == "printers_higher":
            q6 = self.player.printers_higher
        elif participant.vars['qs_order2'][1] == "laptops_higher":
            q6 = self.player.laptops_higher
        else:
            # participant.vars['qs_order2'][1] == "tickets_higher":
            q6 = self.player.tickets_higher

        if q5 is not None and q6 is not None and self.player.participant.vars['feedback'][0] == "feedback":
            return True

    def vars_for_template(self):
        participant = self.player.participant
        if participant.vars['qs_order'][1] == "germans_lower":
            q5 = self.player.germans_lower
            correct = 2700
        elif participant.vars['qs_order'][1] == "temporary_lower":
            q5 = self.player.temporary_lower
            correct = 2340
        elif participant.vars['qs_order'][1] == "commissioner_lower":
            q5 = self.player.commissioner_lower
            correct = 233
        elif participant.vars['qs_order'][1] == "age_lower":
            q5 = self.player.age_lower
            correct = 59
        elif participant.vars['qs_order'][1] == "allowance_lower":
            q5 = self.player.allowance_lower
            correct = 1418
        elif participant.vars['qs_order'][1] == "paper_lower":
            q5 = self.player.paper_lower
            correct = 710
        elif participant.vars['qs_order'][1] == "printers_lower":
            q5 = self.player.printers_lower
            correct = 3503
        elif participant.vars['qs_order'][1] == "laptops_lower":
            q5 = self.player.laptops_lower
            correct = 9000
        else:
            # participant.vars['qs_order'][1] == "tickets_lower"
            q5 = self.player.tickets_lower
            correct = 2250

        if participant.vars['qs_order2'][1] == "germans_higher":
            q6 = self.player.germans_higher
        elif participant.vars['qs_order2'][1] == "temporary_higher":
            q6 = self.player.temporary_higher
        elif participant.vars['qs_order2'][1] == "commissioner_higher":
            q6 = self.player.commissioner_higher
        elif participant.vars['qs_order2'][1] == "age_higher":
            q6 = self.player.age_higher
        elif participant.vars['qs_order2'][1] == "allowance_higher":
            q6 = self.player.allowance_higher
        elif participant.vars['qs_order2'][1] == "paper_higher":
            q6 = self.player.paper_higher
        elif participant.vars['qs_order2'][1] == "printers_higher":
            q6 = self.player.printers_higher
        elif participant.vars['qs_order2'][1] == "laptops_higher":
            q6 = self.player.laptops_higher
        else:
            # participant.vars['qs_order2'][1] == "tickets_higher":
            q6 = self.player.tickets_higher

        question1 = self.player.emails_lower
        question2 = self.player.emails_higher
        question3 = self.player.temporary_lower
        question4 = self.player.temporary_higher
        question5 = self.player.commissioner_lower
        question6 = self.player.commissioner_higher
        question7 = self.player.age_lower
        question8 = self.player.age_higher
        question9 = self.player.allowance_lower
        question10 = self.player.allowance_higher
        question11 = self.player.paper_lower
        question12 = self.player.paper_higher
        question13 = self.player.printers_lower
        question14 = self.player.printers_higher
        question15 = self.player.laptops_lower
        question16 = self.player.laptops_higher
        question17 = self.player.tickets_lower
        question18 = self.player.tickets_higher
        question19 = self.player.germans_lower
        question20 = self.player.germans_higher

        if question1 == None:
            question1 = "(skipped)"
        if question2 == None:
            question2 = "(skipped)"
        if question3 == None:
            question3 = "(skipped)"
        if question4 == None:
            question4 = "(skipped)"
        if question5 == None:
            question5 = "(skipped)"
        if question6 == None:
            question6 = "(skipped)"
        if question7 == None:
            question7 = "(skipped)"
        if question8 == None:
            question8 = "(skipped)"
        if question9 == None:
            question9 = "(skipped)"
        if question10 == None:
            question10 = "(skipped)"
        if question11 == None:
            question11 = "(skipped)"
        if question12 == None:
            question12 = "(skipped)"
        if question13 == None:
            question13 = "(skipped)"
        if question14 == None:
            question14 = "(skipped)"
        if question15 == None:
            question15 = "(skipped)"
        if question16 == None:
            question16 = "(skipped)"
        if question17 == None:
            question17 = "(skipped)"
        if question18 == None:
            question18 = "(skipped)"
        if question19 == None:
            question19 = "(skipped)"
        if question20 == None:
            question20 = "(skipped)"

        down = [question1, question3, question5, question7, question9, question11, question13, question15, question17,
                question19]
        up = [question2, question4, question6, question8, question10, question12, question14, question16, question18,
              question20]

        correct_answers = [53, 2700, 2340, 233, 59, 1418, 710, 3503, 9000, 2250]
        CORRECT = 0
        for i in range(0, len(correct_answers)):
            try:
                if down[i] <= correct_answers[i] <= up[i]:
                    CORRECT += 1
            except:
                continue

        ANSWERED = 0
        for i in range(0, len(correct_answers)):
            try:
                if down[i] >= 0 and up[i] >= 0:
                    ANSWERED += 1
                elif down[i] >= 0 and up[i] == "(skipped)":
                    ANSWERED += 0
                elif down[i] == "(skipped)" and up[i] >= 0:
                    ANSWERED += 0
                else:
                    ANSWERED += 0
            except:
                continue

        CORRECT = round(CORRECT, 1)
        CORRECT_P = round(ANSWERED * 0.9, 1)
        try:
            PERCENT = round(100 * CORRECT / ANSWERED, 1)
        except:
            PERCENT = 0

        return dict(
            CORRECT=CORRECT,
            CORRECT_P=CORRECT_P,
            ANSWERED=ANSWERED,
            PERCENT=PERCENT,
            q5=q5,
            q6=q6,
            correct=correct,
        )


class Q4(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        set3 = [participant.vars['qs_order'][2], participant.vars['qs_order2'][2],
                'skip_all']
        return set3

    def is_displayed(self):
        if self.player.skip_all == True:
            return True

    def error_message(self, values):
        participant = self.player.participant
        print('values is', values)
        try:
            if values[participant.vars['qs_order'][2]] >= values[participant.vars['qs_order2'][2]]:
                return "When you claim that the number we asked about is between A and B, please make sure that your B is larger than A."
        except:
            pass


class Q4feedback(Page):
    form_model = 'player'

    def is_displayed(self):
        participant = self.player.participant
        if participant.vars['qs_order'][2] == "germans_lower":
            q7 = self.player.germans_lower
        elif participant.vars['qs_order'][2] == "temporary_lower":
            q7 = self.player.temporary_lower
        elif participant.vars['qs_order'][2] == "commissioner_lower":
            q7 = self.player.commissioner_lower
        elif participant.vars['qs_order'][2] == "age_lower":
            q7 = self.player.age_lower
        elif participant.vars['qs_order'][2] == "allowance_lower":
            q7 = self.player.allowance_lower
        elif participant.vars['qs_order'][2] == "paper_lower":
            q7 = self.player.paper_lower
        elif participant.vars['qs_order'][2] == "printers_lower":
            q7 = self.player.printers_lower
        elif participant.vars['qs_order'][2] == "laptops_lower":
            q7 = self.player.laptops_lower
        else:
            # participant.vars['qs_order'][2] == "tickets_lower"
            q7 = self.player.tickets_lower

        if participant.vars['qs_order2'][2] == "germans_higher":
            q8 = self.player.germans_higher
        elif participant.vars['qs_order2'][2] == "temporary_higher":
            q8 = self.player.temporary_higher
        elif participant.vars['qs_order2'][2] == "commissioner_higher":
            q8 = self.player.commissioner_higher
        elif participant.vars['qs_order2'][2] == "age_higher":
            q8 = self.player.age_higher
        elif participant.vars['qs_order2'][2] == "allowance_higher":
            q8 = self.player.allowance_higher
        elif participant.vars['qs_order2'][2] == "paper_higher":
            q8 = self.player.paper_higher
        elif participant.vars['qs_order2'][2] == "printers_higher":
            q8 = self.player.printers_higher
        elif participant.vars['qs_order2'][2] == "laptops_higher":
            q8 = self.player.laptops_higher
        else:
            # participant.vars['qs_order2'][2] == "tickets_higher":
            q8 = self.player.tickets_higher

        if q7 is not None and q8 is not None and self.player.participant.vars['feedback'][0] == "feedback":
            return True

    def vars_for_template(self):
        participant = self.player.participant
        if participant.vars['qs_order'][2] == "germans_lower":
            q7 = self.player.germans_lower
            correct = 2700
        elif participant.vars['qs_order'][2] == "temporary_lower":
            q7 = self.player.temporary_lower
            correct = 2340
        elif participant.vars['qs_order'][2] == "commissioner_lower":
            q7 = self.player.commissioner_lower
            correct = 233
        elif participant.vars['qs_order'][2] == "age_lower":
            q7 = self.player.age_lower
            correct = 59
        elif participant.vars['qs_order'][2] == "allowance_lower":
            q7 = self.player.allowance_lower
            correct = 1418
        elif participant.vars['qs_order'][2] == "paper_lower":
            q7 = self.player.paper_lower
            correct = 710
        elif participant.vars['qs_order'][2] == "printers_lower":
            q7 = self.player.printers_lower
            correct = 3503
        elif participant.vars['qs_order'][2] == "laptops_lower":
            q7 = self.player.laptops_lower
            correct = 9000
        else:
            # participant.vars['qs_order'][2] == "tickets_lower"
            q7 = self.player.tickets_lower
            correct = 2250

        if participant.vars['qs_order2'][2] == "germans_higher":
            q8 = self.player.germans_higher
        elif participant.vars['qs_order2'][2] == "temporary_higher":
            q8 = self.player.temporary_higher
        elif participant.vars['qs_order2'][2] == "commissioner_higher":
            q8 = self.player.commissioner_higher
        elif participant.vars['qs_order2'][2] == "age_higher":
            q8 = self.player.age_higher
        elif participant.vars['qs_order2'][2] == "allowance_higher":
            q8 = self.player.allowance_higher
        elif participant.vars['qs_order2'][2] == "paper_higher":
            q8 = self.player.paper_higher
        elif participant.vars['qs_order2'][2] == "printers_higher":
            q8 = self.player.printers_higher
        elif participant.vars['qs_order2'][2] == "laptops_higher":
            q8 = self.player.laptops_higher
        else:
            # participant.vars['qs_order2'][2] == "tickets_higher":
            q8 = self.player.tickets_higher

        question1 = self.player.emails_lower
        question2 = self.player.emails_higher
        question3 = self.player.temporary_lower
        question4 = self.player.temporary_higher
        question5 = self.player.commissioner_lower
        question6 = self.player.commissioner_higher
        question7 = self.player.age_lower
        question8 = self.player.age_higher
        question9 = self.player.allowance_lower
        question10 = self.player.allowance_higher
        question11 = self.player.paper_lower
        question12 = self.player.paper_higher
        question13 = self.player.printers_lower
        question14 = self.player.printers_higher
        question15 = self.player.laptops_lower
        question16 = self.player.laptops_higher
        question17 = self.player.tickets_lower
        question18 = self.player.tickets_higher
        question19 = self.player.germans_lower
        question20 = self.player.germans_higher

        if question1 == None:
            question1 = "(skipped)"
        if question2 == None:
            question2 = "(skipped)"
        if question3 == None:
            question3 = "(skipped)"
        if question4 == None:
            question4 = "(skipped)"
        if question5 == None:
            question5 = "(skipped)"
        if question6 == None:
            question6 = "(skipped)"
        if question7 == None:
            question7 = "(skipped)"
        if question8 == None:
            question8 = "(skipped)"
        if question9 == None:
            question9 = "(skipped)"
        if question10 == None:
            question10 = "(skipped)"
        if question11 == None:
            question11 = "(skipped)"
        if question12 == None:
            question12 = "(skipped)"
        if question13 == None:
            question13 = "(skipped)"
        if question14 == None:
            question14 = "(skipped)"
        if question15 == None:
            question15 = "(skipped)"
        if question16 == None:
            question16 = "(skipped)"
        if question17 == None:
            question17 = "(skipped)"
        if question18 == None:
            question18 = "(skipped)"
        if question19 == None:
            question19 = "(skipped)"
        if question20 == None:
            question20 = "(skipped)"

        down = [question1, question3, question5, question7, question9, question11, question13, question15, question17,
                question19]
        up = [question2, question4, question6, question8, question10, question12, question14, question16, question18,
              question20]

        correct_answers = [53, 2700, 2340, 233, 59, 1418, 710, 3503, 9000, 2250]
        CORRECT = 0
        for i in range(0, len(correct_answers)):
            try:
                if down[i] <= correct_answers[i] <= up[i]:
                    CORRECT += 1
            except:
                continue

        ANSWERED = 0
        for i in range(0, len(correct_answers)):
            try:
                if down[i] >= 0 and up[i] >= 0:
                    ANSWERED += 1
                elif down[i] >= 0 and up[i] == "(skipped)":
                    ANSWERED += 0
                elif down[i] == "(skipped)" and up[i] >= 0:
                    ANSWERED += 0
                else:
                    ANSWERED += 0
            except:
                continue

        CORRECT = round(CORRECT, 1)
        CORRECT_P = round(ANSWERED * 0.9, 1)
        try:
            PERCENT = round(100 * CORRECT / ANSWERED, 1)
        except:
            PERCENT = 0

        return dict(
            CORRECT=CORRECT,
            CORRECT_P=CORRECT_P,
            ANSWERED=ANSWERED,
            PERCENT=PERCENT,
            q7=q7,
            q8=q8,
            correct=correct,
        )


class Q5(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        set4 = [participant.vars['qs_order'][3], participant.vars['qs_order2'][3],
                'skip_all']
        return set4

    def is_displayed(self):
        if self.player.skip_all == True:
            return True

    def error_message(self, values):
        participant = self.player.participant
        print('values is', values)
        try:
            if values[participant.vars['qs_order'][3]] >= values[participant.vars['qs_order2'][3]]:
                return "When you claim that the number we asked about is between A and B, please make sure that your " \
                       "B is larger than A. "
        except:
            pass


class Q5feedback(Page):
    form_model = 'player'

    def is_displayed(self):
        participant = self.player.participant
        if participant.vars['qs_order'][3] == "germans_lower":
            q9 = self.player.germans_lower
        elif participant.vars['qs_order'][3] == "temporary_lower":
            q9 = self.player.temporary_lower
        elif participant.vars['qs_order'][3] == "commissioner_lower":
            q9 = self.player.commissioner_lower
        elif participant.vars['qs_order'][3] == "age_lower":
            q9 = self.player.age_lower
        elif participant.vars['qs_order'][3] == "allowance_lower":
            q9 = self.player.allowance_lower
        elif participant.vars['qs_order'][3] == "paper_lower":
            q9 = self.player.paper_lower
        elif participant.vars['qs_order'][3] == "printers_lower":
            q9 = self.player.printers_lower
        elif participant.vars['qs_order'][3] == "laptops_lower":
            q9 = self.player.laptops_lower
        else:
            # participant.vars['qs_order'][3] == "tickets_lower"
            q9 = self.player.tickets_lower

        if participant.vars['qs_order2'][3] == "germans_higher":
            q10 = self.player.germans_higher
        elif participant.vars['qs_order2'][3] == "temporary_higher":
            q10 = self.player.temporary_higher
        elif participant.vars['qs_order2'][3] == "commissioner_higher":
            q10 = self.player.commissioner_higher
        elif participant.vars['qs_order2'][3] == "age_higher":
            q10 = self.player.age_higher
        elif participant.vars['qs_order2'][3] == "allowance_higher":
            q10 = self.player.allowance_higher
        elif participant.vars['qs_order2'][3] == "paper_higher":
            q10 = self.player.paper_higher
        elif participant.vars['qs_order2'][3] == "printers_higher":
            q10 = self.player.printers_higher
        elif participant.vars['qs_order2'][3] == "laptops_higher":
            q10 = self.player.laptops_higher
        else:
            # participant.vars['qs_order2'][3] == "tickets_higher":
            q10 = self.player.tickets_higher

        if q9 is not None and q10 is not None and self.player.participant.vars['feedback'][0] == "feedback":
            return True

    def vars_for_template(self):
        participant = self.player.participant
        if participant.vars['qs_order'][3] == "germans_lower":
            q9 = self.player.germans_lower
            correct = 2700
        elif participant.vars['qs_order'][3] == "temporary_lower":
            q9 = self.player.temporary_lower
            correct = 2340
        elif participant.vars['qs_order'][3] == "commissioner_lower":
            q9 = self.player.commissioner_lower
            correct = 233
        elif participant.vars['qs_order'][3] == "age_lower":
            q9 = self.player.age_lower
            correct = 59
        elif participant.vars['qs_order'][3] == "allowance_lower":
            q9 = self.player.allowance_lower
            correct = 1418
        elif participant.vars['qs_order'][3] == "paper_lower":
            q9 = self.player.paper_lower
            correct = 710
        elif participant.vars['qs_order'][3] == "printers_lower":
            q9 = self.player.printers_lower
            correct = 3503
        elif participant.vars['qs_order'][3] == "laptops_lower":
            q9 = self.player.laptops_lower
            correct = 9000
        else:
            # participant.vars['qs_order'][3] == "tickets_lower"
            q9 = self.player.tickets_lower
            correct = 2250

        if participant.vars['qs_order2'][3] == "germans_higher":
            q10 = self.player.germans_higher
        elif participant.vars['qs_order2'][3] == "temporary_higher":
            q10 = self.player.temporary_higher
        elif participant.vars['qs_order2'][3] == "commissioner_higher":
            q10 = self.player.commissioner_higher
        elif participant.vars['qs_order2'][3] == "age_higher":
            q10 = self.player.age_higher
        elif participant.vars['qs_order2'][3] == "allowance_higher":
            q10 = self.player.allowance_higher
        elif participant.vars['qs_order2'][3] == "paper_higher":
            q10 = self.player.paper_higher
        elif participant.vars['qs_order2'][3] == "printers_higher":
            q10 = self.player.printers_higher
        elif participant.vars['qs_order2'][3] == "laptops_higher":
            q10 = self.player.laptops_higher
        else:
            # participant.vars['qs_order2'][3] == "tickets_higher":
            q10 = self.player.tickets_higher

        question1 = self.player.emails_lower
        question2 = self.player.emails_higher
        question3 = self.player.temporary_lower
        question4 = self.player.temporary_higher
        question5 = self.player.commissioner_lower
        question6 = self.player.commissioner_higher
        question7 = self.player.age_lower
        question8 = self.player.age_higher
        question9 = self.player.allowance_lower
        question10 = self.player.allowance_higher
        question11 = self.player.paper_lower
        question12 = self.player.paper_higher
        question13 = self.player.printers_lower
        question14 = self.player.printers_higher
        question15 = self.player.laptops_lower
        question16 = self.player.laptops_higher
        question17 = self.player.tickets_lower
        question18 = self.player.tickets_higher
        question19 = self.player.germans_lower
        question20 = self.player.germans_higher

        if question1 == None:
            question1 = "(skipped)"
        if question2 == None:
            question2 = "(skipped)"
        if question3 == None:
            question3 = "(skipped)"
        if question4 == None:
            question4 = "(skipped)"
        if question5 == None:
            question5 = "(skipped)"
        if question6 == None:
            question6 = "(skipped)"
        if question7 == None:
            question7 = "(skipped)"
        if question8 == None:
            question8 = "(skipped)"
        if question9 == None:
            question9 = "(skipped)"
        if question10 == None:
            question10 = "(skipped)"
        if question11 == None:
            question11 = "(skipped)"
        if question12 == None:
            question12 = "(skipped)"
        if question13 == None:
            question13 = "(skipped)"
        if question14 == None:
            question14 = "(skipped)"
        if question15 == None:
            question15 = "(skipped)"
        if question16 == None:
            question16 = "(skipped)"
        if question17 == None:
            question17 = "(skipped)"
        if question18 == None:
            question18 = "(skipped)"
        if question19 == None:
            question19 = "(skipped)"
        if question20 == None:
            question20 = "(skipped)"

        down = [question1, question3, question5, question7, question9, question11, question13, question15, question17,
                question19]
        up = [question2, question4, question6, question8, question10, question12, question14, question16, question18,
              question20]

        correct_answers = [53, 2700, 2340, 233, 59, 1418, 710, 3503, 9000, 2250]
        CORRECT = 0
        for i in range(0, len(correct_answers)):
            try:
                if down[i] <= correct_answers[i] <= up[i]:
                    CORRECT += 1
            except:
                continue

        ANSWERED = 0
        for i in range(0, len(correct_answers)):
            try:
                if down[i] >= 0 and up[i] >= 0:
                    ANSWERED += 1
                elif down[i] >= 0 and up[i] == "(skipped)":
                    ANSWERED += 0
                elif down[i] == "(skipped)" and up[i] >= 0:
                    ANSWERED += 0
                else:
                    ANSWERED += 0
            except:
                continue

        CORRECT = round(CORRECT, 1)
        CORRECT_P = round(ANSWERED * 0.9, 1)
        try:
            PERCENT = round(100 * CORRECT / ANSWERED, 1)
        except:
            PERCENT = 0

        return dict(
            CORRECT=CORRECT,
            CORRECT_P=CORRECT_P,
            ANSWERED=ANSWERED,
            PERCENT=PERCENT,
            q9=q9,
            q10=q10,
            correct=correct,
        )


class Q6(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        set5 = [participant.vars['qs_order'][4], participant.vars['qs_order2'][4],
                'skip_all']
        return set5

    def is_displayed(self):
        if self.player.skip_all == True:
            return True

    def error_message(self, values):
        participant = self.player.participant
        print('values is', values)
        try:
            if values[participant.vars['qs_order'][4]] >= values[participant.vars['qs_order2'][4]]:
                return "When you claim that the number we asked about is between A and B, please make sure that your " \
                       "B is larger than A. "
        except:
            pass


class Q6feedback(Page):
    form_model = 'player'

    def is_displayed(self):
        participant = self.player.participant
        if participant.vars['qs_order'][4] == "germans_lower":
            q11 = self.player.germans_lower
        elif participant.vars['qs_order'][4] == "temporary_lower":
            q11 = self.player.temporary_lower
        elif participant.vars['qs_order'][4] == "commissioner_lower":
            q11 = self.player.commissioner_lower
        elif participant.vars['qs_order'][4] == "age_lower":
            q11 = self.player.age_lower
        elif participant.vars['qs_order'][4] == "allowance_lower":
            q11 = self.player.allowance_lower
        elif participant.vars['qs_order'][4] == "paper_lower":
            q11 = self.player.paper_lower
        elif participant.vars['qs_order'][4] == "printers_lower":
            q11 = self.player.printers_lower
        elif participant.vars['qs_order'][4] == "laptops_lower":
            q11 = self.player.laptops_lower
        else:
            # participant.vars['qs_order'][4] == "tickets_lower"
            q11 = self.player.tickets_lower

        if participant.vars['qs_order2'][4] == "germans_higher":
            q12 = self.player.germans_higher
        elif participant.vars['qs_order2'][4] == "temporary_higher":
            q12 = self.player.temporary_higher
        elif participant.vars['qs_order2'][4] == "commissioner_higher":
            q12 = self.player.commissioner_higher
        elif participant.vars['qs_order2'][4] == "age_higher":
            q12 = self.player.age_higher
        elif participant.vars['qs_order2'][4] == "allowance_higher":
            q12 = self.player.allowance_higher
        elif participant.vars['qs_order2'][4] == "paper_higher":
            q12 = self.player.paper_higher
        elif participant.vars['qs_order2'][4] == "printers_higher":
            q12 = self.player.printers_higher
        elif participant.vars['qs_order2'][4] == "laptops_higher":
            q12 = self.player.laptops_higher
        else:
            # participant.vars['qs_order2'][4] == "tickets_higher":
            q12 = self.player.tickets_higher

        if q11 is not None and q12 is not None and self.player.participant.vars['feedback'][0] == "feedback":
            return True

    def vars_for_template(self):
        participant = self.player.participant
        if participant.vars['qs_order'][4] == "germans_lower":
            q11 = self.player.germans_lower
            correct = 2700
        elif participant.vars['qs_order'][4] == "temporary_lower":
            q11 = self.player.temporary_lower
            correct = 2340
        elif participant.vars['qs_order'][4] == "commissioner_lower":
            q11 = self.player.commissioner_lower
            correct = 233
        elif participant.vars['qs_order'][4] == "age_lower":
            q11 = self.player.age_lower
            correct = 59
        elif participant.vars['qs_order'][4] == "allowance_lower":
            q11 = self.player.allowance_lower
            correct = 1418
        elif participant.vars['qs_order'][4] == "paper_lower":
            q11 = self.player.paper_lower
            correct = 710
        elif participant.vars['qs_order'][4] == "printers_lower":
            q11 = self.player.printers_lower
            correct = 3503
        elif participant.vars['qs_order'][4] == "laptops_lower":
            q11 = self.player.laptops_lower
            correct = 9000
        else:
            # participant.vars['qs_order'][4] == "tickets_lower"
            q11 = self.player.tickets_lower
            correct = 2250

        if participant.vars['qs_order2'][4] == "germans_higher":
            q12 = self.player.germans_higher
        elif participant.vars['qs_order2'][4] == "temporary_higher":
            q12 = self.player.temporary_higher
        elif participant.vars['qs_order2'][4] == "commissioner_higher":
            q12 = self.player.commissioner_higher
        elif participant.vars['qs_order2'][4] == "age_higher":
            q12 = self.player.age_higher
        elif participant.vars['qs_order2'][4] == "allowance_higher":
            q12 = self.player.allowance_higher
        elif participant.vars['qs_order2'][4] == "paper_higher":
            q12 = self.player.paper_higher
        elif participant.vars['qs_order2'][4] == "printers_higher":
            q12 = self.player.printers_higher
        elif participant.vars['qs_order2'][4] == "laptops_higher":
            q12 = self.player.laptops_higher
        else:
            # participant.vars['qs_order2'][4] == "tickets_higher":
            q12 = self.player.tickets_higher

        question1 = self.player.emails_lower
        question2 = self.player.emails_higher
        question3 = self.player.temporary_lower
        question4 = self.player.temporary_higher
        question5 = self.player.commissioner_lower
        question6 = self.player.commissioner_higher
        question7 = self.player.age_lower
        question8 = self.player.age_higher
        question9 = self.player.allowance_lower
        question10 = self.player.allowance_higher
        question11 = self.player.paper_lower
        question12 = self.player.paper_higher
        question13 = self.player.printers_lower
        question14 = self.player.printers_higher
        question15 = self.player.laptops_lower
        question16 = self.player.laptops_higher
        question17 = self.player.tickets_lower
        question18 = self.player.tickets_higher
        question19 = self.player.germans_lower
        question20 = self.player.germans_higher

        if question1 == None:
            question1 = "(skipped)"
        if question2 == None:
            question2 = "(skipped)"
        if question3 == None:
            question3 = "(skipped)"
        if question4 == None:
            question4 = "(skipped)"
        if question5 == None:
            question5 = "(skipped)"
        if question6 == None:
            question6 = "(skipped)"
        if question7 == None:
            question7 = "(skipped)"
        if question8 == None:
            question8 = "(skipped)"
        if question9 == None:
            question9 = "(skipped)"
        if question10 == None:
            question10 = "(skipped)"
        if question11 == None:
            question11 = "(skipped)"
        if question12 == None:
            question12 = "(skipped)"
        if question13 == None:
            question13 = "(skipped)"
        if question14 == None:
            question14 = "(skipped)"
        if question15 == None:
            question15 = "(skipped)"
        if question16 == None:
            question16 = "(skipped)"
        if question17 == None:
            question17 = "(skipped)"
        if question18 == None:
            question18 = "(skipped)"
        if question19 == None:
            question19 = "(skipped)"
        if question20 == None:
            question20 = "(skipped)"

        down = [question1, question3, question5, question7, question9, question11, question13, question15, question17,
                question19]
        up = [question2, question4, question6, question8, question10, question12, question14, question16, question18,
              question20]

        correct_answers = [53, 2700, 2340, 233, 59, 1418, 710, 3503, 9000, 2250]
        CORRECT = 0
        for i in range(0, len(correct_answers)):
            try:
                if down[i] <= correct_answers[i] <= up[i]:
                    CORRECT += 1
            except:
                continue

        ANSWERED = 0
        for i in range(0, len(correct_answers)):
            try:
                if down[i] >= 0 and up[i] >= 0:
                    ANSWERED += 1
                elif down[i] >= 0 and up[i] == "(skipped)":
                    ANSWERED += 0
                elif down[i] == "(skipped)" and up[i] >= 0:
                    ANSWERED += 0
                else:
                    ANSWERED += 0
            except:
                continue

        CORRECT = round(CORRECT, 1)
        CORRECT_P = round(ANSWERED * 0.9, 1)
        try:
            PERCENT = round(100 * CORRECT / ANSWERED, 1)
        except:
            PERCENT = 0

        return dict(
            CORRECT=CORRECT,
            CORRECT_P=CORRECT_P,
            ANSWERED=ANSWERED,
            PERCENT=PERCENT,
            q11=q11,
            q12=q12,
            correct=correct,
        )


class Q7(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        set6 = [participant.vars['qs_order'][5], participant.vars['qs_order2'][5],
                'skip_all']
        return set6

    def is_displayed(self):
        if self.player.skip_all == True:
            return True

    def error_message(self, values):
        participant = self.player.participant
        print('values is', values)
        try:
            if values[participant.vars['qs_order'][5]] >= values[participant.vars['qs_order2'][5]]:
                return "When you claim that the number we asked about is between A and B, please make sure that your B is larger than A."
        except:
            pass


class Q7feedback(Page):
    form_model = 'player'

    def is_displayed(self):
        participant = self.player.participant
        if participant.vars['qs_order'][5] == "germans_lower":
            q13 = self.player.germans_lower
        elif participant.vars['qs_order'][5] == "temporary_lower":
            q13 = self.player.temporary_lower
        elif participant.vars['qs_order'][5] == "commissioner_lower":
            q13 = self.player.commissioner_lower
        elif participant.vars['qs_order'][5] == "age_lower":
            q13 = self.player.age_lower
        elif participant.vars['qs_order'][5] == "allowance_lower":
            q13 = self.player.allowance_lower
        elif participant.vars['qs_order'][5] == "paper_lower":
            q13 = self.player.paper_lower
        elif participant.vars['qs_order'][5] == "printers_lower":
            q13 = self.player.printers_lower
        elif participant.vars['qs_order'][5] == "laptops_lower":
            q13 = self.player.laptops_lower
        else:
            # participant.vars['qs_order'][5] == "tickets_lower"
            q13 = self.player.tickets_lower

        if participant.vars['qs_order2'][5] == "germans_higher":
            q14 = self.player.germans_higher
        elif participant.vars['qs_order2'][5] == "temporary_higher":
            q14 = self.player.temporary_higher
        elif participant.vars['qs_order2'][5] == "commissioner_higher":
            q14 = self.player.commissioner_higher
        elif participant.vars['qs_order2'][5] == "age_higher":
            q14 = self.player.age_higher
        elif participant.vars['qs_order2'][5] == "allowance_higher":
            q14 = self.player.allowance_higher
        elif participant.vars['qs_order2'][5] == "paper_higher":
            q14 = self.player.paper_higher
        elif participant.vars['qs_order2'][5] == "printers_higher":
            q14 = self.player.printers_higher
        elif participant.vars['qs_order2'][5] == "laptops_higher":
            q14 = self.player.laptops_higher
        else:
            # participant.vars['qs_order2'][5] == "tickets_higher":
            q14 = self.player.tickets_higher

        if q13 is not None and q14 is not None and self.player.participant.vars['feedback'][0] == "feedback":
            return True

    def vars_for_template(self):
        participant = self.player.participant
        if participant.vars['qs_order'][5] == "germans_lower":
            q13 = self.player.germans_lower
            correct = 2700
        elif participant.vars['qs_order'][5] == "temporary_lower":
            q13 = self.player.temporary_lower
            correct = 2340
        elif participant.vars['qs_order'][5] == "commissioner_lower":
            q13 = self.player.commissioner_lower
            correct = 233
        elif participant.vars['qs_order'][5] == "age_lower":
            q13 = self.player.age_lower
            correct = 59
        elif participant.vars['qs_order'][5] == "allowance_lower":
            q13 = self.player.allowance_lower
            correct = 1418
        elif participant.vars['qs_order'][5] == "paper_lower":
            q13 = self.player.paper_lower
            correct = 710
        elif participant.vars['qs_order'][5] == "printers_lower":
            q13 = self.player.printers_lower
            correct = 3503
        elif participant.vars['qs_order'][5] == "laptops_lower":
            q13 = self.player.laptops_lower
            correct = 9000
        else:
            # participant.vars['qs_order'][5] == "tickets_lower"
            q13 = self.player.tickets_lower
            correct = 2250

        if participant.vars['qs_order2'][5] == "germans_higher":
            q14 = self.player.germans_higher
        elif participant.vars['qs_order2'][5] == "temporary_higher":
            q14 = self.player.temporary_higher
        elif participant.vars['qs_order2'][5] == "commissioner_higher":
            q14 = self.player.commissioner_higher
        elif participant.vars['qs_order2'][5] == "age_higher":
            q14 = self.player.age_higher
        elif participant.vars['qs_order2'][5] == "allowance_higher":
            q14 = self.player.allowance_higher
        elif participant.vars['qs_order2'][5] == "paper_higher":
            q14 = self.player.paper_higher
        elif participant.vars['qs_order2'][5] == "printers_higher":
            q14 = self.player.printers_higher
        elif participant.vars['qs_order2'][5] == "laptops_higher":
            q14 = self.player.laptops_higher
        else:
            # participant.vars['qs_order2'][5] == "tickets_higher":
            q14 = self.player.tickets_higher

        question1 = self.player.emails_lower
        question2 = self.player.emails_higher
        question3 = self.player.temporary_lower
        question4 = self.player.temporary_higher
        question5 = self.player.commissioner_lower
        question6 = self.player.commissioner_higher
        question7 = self.player.age_lower
        question8 = self.player.age_higher
        question9 = self.player.allowance_lower
        question10 = self.player.allowance_higher
        question11 = self.player.paper_lower
        question12 = self.player.paper_higher
        question13 = self.player.printers_lower
        question14 = self.player.printers_higher
        question15 = self.player.laptops_lower
        question16 = self.player.laptops_higher
        question17 = self.player.tickets_lower
        question18 = self.player.tickets_higher
        question19 = self.player.germans_lower
        question20 = self.player.germans_higher

        if question1 == None:
            question1 = "(skipped)"
        if question2 == None:
            question2 = "(skipped)"
        if question3 == None:
            question3 = "(skipped)"
        if question4 == None:
            question4 = "(skipped)"
        if question5 == None:
            question5 = "(skipped)"
        if question6 == None:
            question6 = "(skipped)"
        if question7 == None:
            question7 = "(skipped)"
        if question8 == None:
            question8 = "(skipped)"
        if question9 == None:
            question9 = "(skipped)"
        if question10 == None:
            question10 = "(skipped)"
        if question11 == None:
            question11 = "(skipped)"
        if question12 == None:
            question12 = "(skipped)"
        if question13 == None:
            question13 = "(skipped)"
        if question14 == None:
            question14 = "(skipped)"
        if question15 == None:
            question15 = "(skipped)"
        if question16 == None:
            question16 = "(skipped)"
        if question17 == None:
            question17 = "(skipped)"
        if question18 == None:
            question18 = "(skipped)"
        if question19 == None:
            question19 = "(skipped)"
        if question20 == None:
            question20 = "(skipped)"

        down = [question1, question3, question5, question7, question9, question11, question13, question15, question17,
                question19]
        up = [question2, question4, question6, question8, question10, question12, question14, question16, question18,
              question20]

        correct_answers = [53, 2700, 2340, 233, 59, 1418, 710, 3503, 9000, 2250]
        CORRECT = 0
        for i in range(0, len(correct_answers)):
            try:
                if down[i] <= correct_answers[i] <= up[i]:
                    CORRECT += 1
            except:
                continue

        ANSWERED = 0
        for i in range(0, len(correct_answers)):
            try:
                if down[i] >= 0 and up[i] >= 0:
                    ANSWERED += 1
                elif down[i] >= 0 and up[i] == "(skipped)":
                    ANSWERED += 0
                elif down[i] == "(skipped)" and up[i] >= 0:
                    ANSWERED += 0
                else:
                    ANSWERED += 0
            except:
                continue

        CORRECT = round(CORRECT, 1)
        CORRECT_P = round(ANSWERED * 0.9, 1)
        try:
            PERCENT = round(100 * CORRECT / ANSWERED, 1)
        except:
            PERCENT = 0

        return dict(
            CORRECT=CORRECT,
            CORRECT_P=CORRECT_P,
            ANSWERED=ANSWERED,
            PERCENT=PERCENT,
            q13=q13,
            q14=q14,
            correct=correct,
        )


class Q8(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        set7 = [participant.vars['qs_order'][6], participant.vars['qs_order2'][6],
                'skip_all']
        return set7

    def is_displayed(self):
        if self.player.skip_all == True:
            return True

    def error_message(self, values):
        participant = self.player.participant
        print('values is', values)
        try:
            if values[participant.vars['qs_order'][6]] >= values[participant.vars['qs_order2'][6]]:
                return "When you claim that the number we asked about is between A and B, please make sure that your " \
                       "B is larger than A. "
        except:
            pass


class Q8feedback(Page):
    form_model = 'player'

    def is_displayed(self):
        participant = self.player.participant
        if participant.vars['qs_order'][6] == "germans_lower":
            q15 = self.player.germans_lower
        elif participant.vars['qs_order'][6] == "temporary_lower":
            q15 = self.player.temporary_lower
        elif participant.vars['qs_order'][6] == "commissioner_lower":
            q15 = self.player.commissioner_lower
        elif participant.vars['qs_order'][6] == "age_lower":
            q15 = self.player.age_lower
        elif participant.vars['qs_order'][6] == "allowance_lower":
            q15 = self.player.allowance_lower
        elif participant.vars['qs_order'][6] == "paper_lower":
            q15 = self.player.paper_lower
        elif participant.vars['qs_order'][6] == "printers_lower":
            q15 = self.player.printers_lower
        elif participant.vars['qs_order'][6] == "laptops_lower":
            q15 = self.player.laptops_lower
        else:
            # participant.vars['qs_order'][6] == "tickets_lower"
            q15 = self.player.tickets_lower

        if participant.vars['qs_order2'][6] == "germans_higher":
            q16 = self.player.germans_higher
        elif participant.vars['qs_order2'][6] == "temporary_higher":
            q16 = self.player.temporary_higher
        elif participant.vars['qs_order2'][6] == "commissioner_higher":
            q16 = self.player.commissioner_higher
        elif participant.vars['qs_order2'][6] == "age_higher":
            q16 = self.player.age_higher
        elif participant.vars['qs_order2'][6] == "allowance_higher":
            q16 = self.player.allowance_higher
        elif participant.vars['qs_order2'][6] == "paper_higher":
            q16 = self.player.paper_higher
        elif participant.vars['qs_order2'][6] == "printers_higher":
            q16 = self.player.printers_higher
        elif participant.vars['qs_order2'][6] == "laptops_higher":
            q16 = self.player.laptops_higher
        else:
            # participant.vars['qs_order2'][6] == "tickets_higher":
            q16 = self.player.tickets_higher

        if q15 is not None and q16 is not None and self.player.participant.vars['feedback'][0] == "feedback":
            return True

    def vars_for_template(self):
        participant = self.player.participant
        if participant.vars['qs_order'][6] == "germans_lower":
            q15 = self.player.germans_lower
            correct = 2700
        elif participant.vars['qs_order'][6] == "temporary_lower":
            q15 = self.player.temporary_lower
            correct = 2340
        elif participant.vars['qs_order'][6] == "commissioner_lower":
            q15 = self.player.commissioner_lower
            correct = 233
        elif participant.vars['qs_order'][6] == "age_lower":
            q15 = self.player.age_lower
            correct = 59
        elif participant.vars['qs_order'][6] == "allowance_lower":
            q15 = self.player.allowance_lower
            correct = 1418
        elif participant.vars['qs_order'][6] == "paper_lower":
            q15 = self.player.paper_lower
            correct = 710
        elif participant.vars['qs_order'][6] == "printers_lower":
            q15 = self.player.printers_lower
            correct = 3503
        elif participant.vars['qs_order'][6] == "laptops_lower":
            q15 = self.player.laptops_lower
            correct = 9000
        else:
            # participant.vars['qs_order'][6] == "tickets_lower"
            q15 = self.player.tickets_lower
            correct = 2250

        if participant.vars['qs_order2'][6] == "germans_higher":
            q16 = self.player.germans_higher
        elif participant.vars['qs_order2'][6] == "temporary_higher":
            q16 = self.player.temporary_higher
        elif participant.vars['qs_order2'][6] == "commissioner_higher":
            q16 = self.player.commissioner_higher
        elif participant.vars['qs_order2'][6] == "age_higher":
            q16 = self.player.age_higher
        elif participant.vars['qs_order2'][6] == "allowance_higher":
            q16 = self.player.allowance_higher
        elif participant.vars['qs_order2'][6] == "paper_higher":
            q16 = self.player.paper_higher
        elif participant.vars['qs_order2'][6] == "printers_higher":
            q16 = self.player.printers_higher
        elif participant.vars['qs_order2'][6] == "laptops_higher":
            q16 = self.player.laptops_higher
        else:
            # participant.vars['qs_order2'][6] == "tickets_higher":
            q16 = self.player.tickets_higher

        question1 = self.player.emails_lower
        question2 = self.player.emails_higher
        question3 = self.player.temporary_lower
        question4 = self.player.temporary_higher
        question5 = self.player.commissioner_lower
        question6 = self.player.commissioner_higher
        question7 = self.player.age_lower
        question8 = self.player.age_higher
        question9 = self.player.allowance_lower
        question10 = self.player.allowance_higher
        question11 = self.player.paper_lower
        question12 = self.player.paper_higher
        question13 = self.player.printers_lower
        question14 = self.player.printers_higher
        question15 = self.player.laptops_lower
        question16 = self.player.laptops_higher
        question17 = self.player.tickets_lower
        question18 = self.player.tickets_higher
        question19 = self.player.germans_lower
        question20 = self.player.germans_higher

        if question1 == None:
            question1 = "(skipped)"
        if question2 == None:
            question2 = "(skipped)"
        if question3 == None:
            question3 = "(skipped)"
        if question4 == None:
            question4 = "(skipped)"
        if question5 == None:
            question5 = "(skipped)"
        if question6 == None:
            question6 = "(skipped)"
        if question7 == None:
            question7 = "(skipped)"
        if question8 == None:
            question8 = "(skipped)"
        if question9 == None:
            question9 = "(skipped)"
        if question10 == None:
            question10 = "(skipped)"
        if question11 == None:
            question11 = "(skipped)"
        if question12 == None:
            question12 = "(skipped)"
        if question13 == None:
            question13 = "(skipped)"
        if question14 == None:
            question14 = "(skipped)"
        if question15 == None:
            question15 = "(skipped)"
        if question16 == None:
            question16 = "(skipped)"
        if question17 == None:
            question17 = "(skipped)"
        if question18 == None:
            question18 = "(skipped)"
        if question19 == None:
            question19 = "(skipped)"
        if question20 == None:
            question20 = "(skipped)"

        down = [question1, question3, question5, question7, question9, question11, question13, question15, question17,
                question19]
        up = [question2, question4, question6, question8, question10, question12, question14, question16, question18,
              question20]

        correct_answers = [53, 2700, 2340, 233, 59, 1418, 710, 3503, 9000, 2250]
        CORRECT = 0
        for i in range(0, len(correct_answers)):
            try:
                if down[i] <= correct_answers[i] <= up[i]:
                    CORRECT += 1
            except:
                continue

        ANSWERED = 0
        for i in range(0, len(correct_answers)):
            try:
                if down[i] >= 0 and up[i] >= 0:
                    ANSWERED += 1
                elif down[i] >= 0 and up[i] == "(skipped)":
                    ANSWERED += 0
                elif down[i] == "(skipped)" and up[i] >= 0:
                    ANSWERED += 0
                else:
                    ANSWERED += 0
            except:
                continue

        CORRECT = round(CORRECT, 1)
        CORRECT_P = round(ANSWERED * 0.9, 1)
        try:
            PERCENT = round(100 * CORRECT / ANSWERED, 1)
        except:
            PERCENT = 0

        return dict(
            CORRECT=CORRECT,
            CORRECT_P=CORRECT_P,
            ANSWERED=ANSWERED,
            PERCENT=PERCENT,
            q15=q15,
            q16=q16,
            correct=correct,
        )


class Q9(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        set8 = [participant.vars['qs_order'][7], participant.vars['qs_order2'][7],
                'skip_all']
        return set8

    def is_displayed(self):
        if self.player.skip_all == True:
            return True

    def error_message(self, values):
        participant = self.player.participant
        print('values is', values)
        try:
            if values[participant.vars['qs_order'][7]] >= values[participant.vars['qs_order2'][7]]:
                return "When you claim that the number we asked about is between A and B, please make sure that your " \
                       "B is larger than A. "
        except:
            pass


class Q9feedback(Page):
    form_model = 'player'

    def is_displayed(self):
        participant = self.player.participant
        if participant.vars['qs_order'][7] == "germans_lower":
            q17 = self.player.germans_lower
        elif participant.vars['qs_order'][7] == "temporary_lower":
            q17 = self.player.temporary_lower
        elif participant.vars['qs_order'][7] == "commissioner_lower":
            q17 = self.player.commissioner_lower
        elif participant.vars['qs_order'][7] == "age_lower":
            q17 = self.player.age_lower
        elif participant.vars['qs_order'][7] == "allowance_lower":
            q17 = self.player.allowance_lower
        elif participant.vars['qs_order'][7] == "paper_lower":
            q17 = self.player.paper_lower
        elif participant.vars['qs_order'][7] == "printers_lower":
            q17 = self.player.printers_lower
        elif participant.vars['qs_order'][7] == "laptops_lower":
            q17 = self.player.laptops_lower
        else:
            # participant.vars['qs_order'][7] == "tickets_lower"
            q17 = self.player.tickets_lower

        if participant.vars['qs_order2'][7] == "germans_higher":
            q18 = self.player.germans_higher
        elif participant.vars['qs_order2'][7] == "temporary_higher":
            q18 = self.player.temporary_higher
        elif participant.vars['qs_order2'][7] == "commissioner_higher":
            q18 = self.player.commissioner_higher
        elif participant.vars['qs_order2'][7] == "age_higher":
            q18 = self.player.age_higher
        elif participant.vars['qs_order2'][7] == "allowance_higher":
            q18 = self.player.allowance_higher
        elif participant.vars['qs_order2'][7] == "paper_higher":
            q18 = self.player.paper_higher
        elif participant.vars['qs_order2'][7] == "printers_higher":
            q18 = self.player.printers_higher
        elif participant.vars['qs_order2'][7] == "laptops_higher":
            q18 = self.player.laptops_higher
        else:
            # participant.vars['qs_order2'][7] == "tickets_higher":
            q18 = self.player.tickets_higher

        if q17 is not None and q18 is not None and self.player.participant.vars['feedback'][0] == "feedback":
            return True

    def vars_for_template(self):
        participant = self.player.participant
        if participant.vars['qs_order'][7] == "germans_lower":
            q17 = self.player.germans_lower
            correct = 2700
        elif participant.vars['qs_order'][7] == "temporary_lower":
            q17 = self.player.temporary_lower
            correct = 2340
        elif participant.vars['qs_order'][7] == "commissioner_lower":
            q17 = self.player.commissioner_lower
            correct = 233
        elif participant.vars['qs_order'][7] == "age_lower":
            q17 = self.player.age_lower
            correct = 59
        elif participant.vars['qs_order'][7] == "allowance_lower":
            q17 = self.player.allowance_lower
            correct = 1418
        elif participant.vars['qs_order'][7] == "paper_lower":
            q17 = self.player.paper_lower
            correct = 710
        elif participant.vars['qs_order'][7] == "printers_lower":
            q17 = self.player.printers_lower
            correct = 3503
        elif participant.vars['qs_order'][7] == "laptops_lower":
            q17 = self.player.laptops_lower
            correct = 9000
        else:
            # participant.vars['qs_order'][7] == "tickets_lower"
            q17 = self.player.tickets_lower
            correct = 2250

        if participant.vars['qs_order2'][7] == "germans_higher":
            q18 = self.player.germans_higher
        elif participant.vars['qs_order2'][7] == "temporary_higher":
            q18 = self.player.temporary_higher
        elif participant.vars['qs_order2'][7] == "commissioner_higher":
            q18 = self.player.commissioner_higher
        elif participant.vars['qs_order2'][7] == "age_higher":
            q18 = self.player.age_higher
        elif participant.vars['qs_order2'][7] == "allowance_higher":
            q18 = self.player.allowance_higher
        elif participant.vars['qs_order2'][7] == "paper_higher":
            q18 = self.player.paper_higher
        elif participant.vars['qs_order2'][7] == "printers_higher":
            q18 = self.player.printers_higher
        elif participant.vars['qs_order2'][7] == "laptops_higher":
            q18 = self.player.laptops_higher
        else:
            # participant.vars['qs_order2'][7] == "tickets_higher":
            q18 = self.player.tickets_higher

        question1 = self.player.emails_lower
        question2 = self.player.emails_higher
        question3 = self.player.temporary_lower
        question4 = self.player.temporary_higher
        question5 = self.player.commissioner_lower
        question6 = self.player.commissioner_higher
        question7 = self.player.age_lower
        question8 = self.player.age_higher
        question9 = self.player.allowance_lower
        question10 = self.player.allowance_higher
        question11 = self.player.paper_lower
        question12 = self.player.paper_higher
        question13 = self.player.printers_lower
        question14 = self.player.printers_higher
        question15 = self.player.laptops_lower
        question16 = self.player.laptops_higher
        question17 = self.player.tickets_lower
        question18 = self.player.tickets_higher
        question19 = self.player.germans_lower
        question20 = self.player.germans_higher

        if question1 == None:
            question1 = "(skipped)"
        if question2 == None:
            question2 = "(skipped)"
        if question3 == None:
            question3 = "(skipped)"
        if question4 == None:
            question4 = "(skipped)"
        if question5 == None:
            question5 = "(skipped)"
        if question6 == None:
            question6 = "(skipped)"
        if question7 == None:
            question7 = "(skipped)"
        if question8 == None:
            question8 = "(skipped)"
        if question9 == None:
            question9 = "(skipped)"
        if question10 == None:
            question10 = "(skipped)"
        if question11 == None:
            question11 = "(skipped)"
        if question12 == None:
            question12 = "(skipped)"
        if question13 == None:
            question13 = "(skipped)"
        if question14 == None:
            question14 = "(skipped)"
        if question15 == None:
            question15 = "(skipped)"
        if question16 == None:
            question16 = "(skipped)"
        if question17 == None:
            question17 = "(skipped)"
        if question18 == None:
            question18 = "(skipped)"
        if question19 == None:
            question19 = "(skipped)"
        if question20 == None:
            question20 = "(skipped)"

        down = [question1, question3, question5, question7, question9, question11, question13, question15, question17,
                question19]
        up = [question2, question4, question6, question8, question10, question12, question14, question16, question18,
              question20]

        correct_answers = [53, 2700, 2340, 233, 59, 1418, 710, 3503, 9000, 2250]
        CORRECT = 0
        for i in range(0, len(correct_answers)):
            try:
                if down[i] <= correct_answers[i] <= up[i]:
                    CORRECT += 1
            except:
                continue

        ANSWERED = 0
        for i in range(0, len(correct_answers)):
            try:
                if down[i] >= 0 and up[i] >= 0:
                    ANSWERED += 1
                elif down[i] >= 0 and up[i] == "(skipped)":
                    ANSWERED += 0
                elif down[i] == "(skipped)" and up[i] >= 0:
                    ANSWERED += 0
                else:
                    ANSWERED += 0
            except:
                continue

        CORRECT = round(CORRECT, 1)
        CORRECT_P = round(ANSWERED * 0.9, 1)
        try:
            PERCENT = round(100 * CORRECT / ANSWERED, 1)
        except:
            PERCENT = 0

        return dict(
            CORRECT=CORRECT,
            CORRECT_P=CORRECT_P,
            ANSWERED=ANSWERED,
            PERCENT=PERCENT,
            q17=q17,
            q18=q18,
            correct=correct,
        )


class Q10(Page):
    form_model = 'player'

    def get_form_fields(self):
        participant = self.player.participant
        set9 = [participant.vars['qs_order'][8], participant.vars['qs_order2'][8],
                'skip_all']
        return set9

    def is_displayed(self):
        if self.player.skip_all == True:
            return True

    def error_message(self, values):
        participant = self.player.participant
        print('values is', values)
        try:
            if values[participant.vars['qs_order'][8]] >= values[participant.vars['qs_order2'][8]]:
                return "When you claim that the number we asked about is between A and B, please make sure that your " \
                       "B is larger than A. "
        except:
            pass


class Q10feedback(Page):
    form_model = 'player'

    def is_displayed(self):
        participant = self.player.participant
        if participant.vars['qs_order'][8] == "germans_lower":
            q19 = self.player.germans_lower
        elif participant.vars['qs_order'][8] == "temporary_lower":
            q19 = self.player.temporary_lower
        elif participant.vars['qs_order'][8] == "commissioner_lower":
            q19 = self.player.commissioner_lower
        elif participant.vars['qs_order'][8] == "age_lower":
            q19 = self.player.age_lower
        elif participant.vars['qs_order'][8] == "allowance_lower":
            q19 = self.player.allowance_lower
        elif participant.vars['qs_order'][8] == "paper_lower":
            q19 = self.player.paper_lower
        elif participant.vars['qs_order'][8] == "printers_lower":
            q19 = self.player.printers_lower
        elif participant.vars['qs_order'][8] == "laptops_lower":
            q19 = self.player.laptops_lower
        else:
            # participant.vars['qs_order'][8] == "tickets_lower"
            q19 = self.player.tickets_lower

        if participant.vars['qs_order2'][8] == "germans_higher":
            q20 = self.player.germans_higher
        elif participant.vars['qs_order2'][8] == "temporary_higher":
            q20 = self.player.temporary_higher
        elif participant.vars['qs_order2'][8] == "commissioner_higher":
            q20 = self.player.commissioner_higher
        elif participant.vars['qs_order2'][8] == "age_higher":
            q20 = self.player.age_higher
        elif participant.vars['qs_order2'][8] == "allowance_higher":
            q20 = self.player.allowance_higher
        elif participant.vars['qs_order2'][8] == "paper_higher":
            q20 = self.player.paper_higher
        elif participant.vars['qs_order2'][8] == "printers_higher":
            q20 = self.player.printers_higher
        elif participant.vars['qs_order2'][8] == "laptops_higher":
            q20 = self.player.laptops_higher
        else:
            # participant.vars['qs_order2'][8] == "tickets_higher":
            q20 = self.player.tickets_higher

        if q19 is not None and q20 is not None and self.player.participant.vars['feedback'][0] == "feedback":
            return True

    def vars_for_template(self):
        participant = self.player.participant
        if participant.vars['qs_order'][8] == "germans_lower":
            q19 = self.player.germans_lower
            correct = 2700
        elif participant.vars['qs_order'][8] == "temporary_lower":
            q19 = self.player.temporary_lower
            correct = 2340
        elif participant.vars['qs_order'][8] == "commissioner_lower":
            q19 = self.player.commissioner_lower
            correct = 233
        elif participant.vars['qs_order'][8] == "age_lower":
            q19 = self.player.age_lower
            correct = 59
        elif participant.vars['qs_order'][8] == "allowance_lower":
            q19 = self.player.allowance_lower
            correct = 1418
        elif participant.vars['qs_order'][8] == "paper_lower":
            q19 = self.player.paper_lower
            correct = 710
        elif participant.vars['qs_order'][8] == "printers_lower":
            q19 = self.player.printers_lower
            correct = 3503
        elif participant.vars['qs_order'][8] == "laptops_lower":
            q19 = self.player.laptops_lower
            correct = 9000
        else:
            # participant.vars['qs_order'][8] == "tickets_lower"
            q19 = self.player.tickets_lower
            correct = 2250

        if participant.vars['qs_order2'][8] == "germans_higher":
            q20 = self.player.germans_higher
        elif participant.vars['qs_order2'][8] == "temporary_higher":
            q20 = self.player.temporary_higher
        elif participant.vars['qs_order2'][8] == "commissioner_higher":
            q20 = self.player.commissioner_higher
        elif participant.vars['qs_order2'][8] == "age_higher":
            q20 = self.player.age_higher
        elif participant.vars['qs_order2'][8] == "allowance_higher":
            q20 = self.player.allowance_higher
        elif participant.vars['qs_order2'][8] == "paper_higher":
            q20 = self.player.paper_higher
        elif participant.vars['qs_order2'][8] == "printers_higher":
            q20 = self.player.printers_higher
        elif participant.vars['qs_order2'][8] == "laptops_higher":
            q20 = self.player.laptops_higher
        else:
            # participant.vars['qs_order2'][8] == "tickets_higher":
            q20 = self.player.tickets_higher

        question1 = self.player.emails_lower
        question2 = self.player.emails_higher
        question3 = self.player.temporary_lower
        question4 = self.player.temporary_higher
        question5 = self.player.commissioner_lower
        question6 = self.player.commissioner_higher
        question7 = self.player.age_lower
        question8 = self.player.age_higher
        question9 = self.player.allowance_lower
        question10 = self.player.allowance_higher
        question11 = self.player.paper_lower
        question12 = self.player.paper_higher
        question13 = self.player.printers_lower
        question14 = self.player.printers_higher
        question15 = self.player.laptops_lower
        question16 = self.player.laptops_higher
        question17 = self.player.tickets_lower
        question18 = self.player.tickets_higher
        question19 = self.player.germans_lower
        question20 = self.player.germans_higher

        if question1 == None:
            question1 = "(skipped)"
        if question2 == None:
            question2 = "(skipped)"
        if question3 == None:
            question3 = "(skipped)"
        if question4 == None:
            question4 = "(skipped)"
        if question5 == None:
            question5 = "(skipped)"
        if question6 == None:
            question6 = "(skipped)"
        if question7 == None:
            question7 = "(skipped)"
        if question8 == None:
            question8 = "(skipped)"
        if question9 == None:
            question9 = "(skipped)"
        if question10 == None:
            question10 = "(skipped)"
        if question11 == None:
            question11 = "(skipped)"
        if question12 == None:
            question12 = "(skipped)"
        if question13 == None:
            question13 = "(skipped)"
        if question14 == None:
            question14 = "(skipped)"
        if question15 == None:
            question15 = "(skipped)"
        if question16 == None:
            question16 = "(skipped)"
        if question17 == None:
            question17 = "(skipped)"
        if question18 == None:
            question18 = "(skipped)"
        if question19 == None:
            question19 = "(skipped)"
        if question20 == None:
            question20 = "(skipped)"

        down = [question1, question3, question5, question7, question9, question11, question13, question15, question17,
                question19]
        up = [question2, question4, question6, question8, question10, question12, question14, question16, question18,
              question20]

        correct_answers = [53, 2340, 233, 59, 1418, 710, 3503, 9000, 2250, 2700]
        CORRECT = 0
        for i in range(0, len(correct_answers)):
            try:
                if down[i] <= correct_answers[i] <= up[i]:
                    CORRECT += 1
            except:
                continue

        ANSWERED = 0
        for i in range(0, len(correct_answers)):
            try:
                if down[i] >= 0 and up[i] >= 0:
                    ANSWERED += 1
                elif down[i] >= 0 and up[i] == "(skipped)":
                    ANSWERED += 0
                elif down[i] == "(skipped)" and up[i] >= 0:
                    ANSWERED += 0
                else:
                    ANSWERED += 0
            except:
                continue

        CORRECT = round(CORRECT, 1)
        CORRECT_P = round(ANSWERED * 0.9, 1)
        try:
            PERCENT = round(100 * CORRECT / ANSWERED, 1)
        except:
            PERCENT = 0

        return dict(
            CORRECT=CORRECT,
            CORRECT_P=CORRECT_P,
            ANSWERED=ANSWERED,
            PERCENT=PERCENT,
            q19=q19,
            q20=q20,
            correct=correct,
        )

        # class Q11(Page):
        #     form_model = 'player'
        #
        #     def get_form_fields(self):
        #         participant = self.player.participant
        #         set10 = [participant.vars['qs_order'][9], participant.vars['qs_order2'][9],
        #                  'skip_all']
        #         return set10
        #
        #     def is_displayed(self):
        #         if self.player.skip_all == True:
        #             return True
        #
        #     def error_message(self, values):
        #         participant = self.player.participant
        #         print('values is', values)
        #         try:
        #             if values[participant.vars['qs_order'][9]] >= values[participant.vars['qs_order2'][9]]:
        #                 return "When you claim that the number we asked about is between A and B, please make sure that your " \
        #                        "B is larger than A. "
        #         except:
        #             pass
        #
        #
        # class Q11feedback(Page):
        #     form_model = 'player'
        #
        #     def is_displayed(self):
        #         participant = self.player.participant
        #         if participant.vars['qs_order'][9] == "germans_lower":
        #             q21 = self.player.germans_lower
        #         elif participant.vars['qs_order'][9] == "temporary_lower":
        #             q21 = self.player.temporary_lower
        #         elif participant.vars['qs_order'][9] == "commissioner_lower":
        #             q21 = self.player.commissioner_lower
        #         elif participant.vars['qs_order'][9] == "age_lower":
        #             q21 = self.player.age_lower
        #         elif participant.vars['qs_order'][9] == "allowance_lower":
        #             q21 = self.player.allowance_lower
        #         elif participant.vars['qs_order'][9] == "paper_lower":
        #             q21 = self.player.paper_lower
        #         elif participant.vars['qs_order'][9] == "printers_lower":
        #             q21 = self.player.printers_lower
        #         elif participant.vars['qs_order'][9] == "laptops_lower":
        #             q21 = self.player.laptops_lower
        #         else:
        #             # participant.vars['qs_order'][9] == "tickets_lower"
        #             q21 = self.player.tickets_lower
        #
        #         if participant.vars['qs_order2'][9] == "germans_higher":
        #             q22 = self.player.germans_higher
        #         elif participant.vars['qs_order2'][9] == "temporary_higher":
        #             q22 = self.player.temporary_higher
        #         elif participant.vars['qs_order2'][9] == "commissioner_higher":
        #             q22 = self.player.commissioner_higher
        #         elif participant.vars['qs_order2'][9] == "age_higher":
        #             q22 = self.player.age_higher
        #         elif participant.vars['qs_order2'][9] == "allowance_higher":
        #             q22 = self.player.allowance_higher
        #         elif participant.vars['qs_order2'][9] == "paper_higher":
        #             q22 = self.player.paper_higher
        #         elif participant.vars['qs_order2'][9] == "printers_higher":
        #             q22 = self.player.printers_higher
        #         elif participant.vars['qs_order2'][9] == "laptops_higher":
        #             q22 = self.player.laptops_higher
        #         else:
        #             # participant.vars['qs_order2'][9] == "tickets_higher":
        #             q22 = self.player.tickets_higher
        #
        #         if q21 is not None and q22 is not None:
        #             return True
        #
        #     def vars_for_template(self):
        #         participant = self.player.participant
        #         if participant.vars['qs_order'][9] == "germans_lower":
        #             q21 = self.player.germans_lower
        #             correct = 2700
        #         elif participant.vars['qs_order'][9] == "temporary_lower":
        #             q21 = self.player.temporary_lower
        #             correct = 2340
        #         elif participant.vars['qs_order'][9] == "commissioner_lower":
        #             q21 = self.player.commissioner_lower
        #             correct = 233
        #         elif participant.vars['qs_order'][9] == "age_lower":
        #             q21 = self.player.age_lower
        #             correct = 59
        #         elif participant.vars['qs_order'][9] == "allowance_lower":
        #             q21 = self.player.allowance_lower
        #             correct = 1418
        #         elif participant.vars['qs_order'][9] == "paper_lower":
        #             q21 = self.player.paper_lower
        #             correct = 710
        #         elif participant.vars['qs_order'][9] == "printers_lower":
        #             q21 = self.player.printers_lower
        #             correct = 3503
        #         elif participant.vars['qs_order'][9] == "laptops_lower":
        #             q21 = self.player.laptops_lower
        #             correct = 9000
        #         else:
        #             # participant.vars['qs_order'][9] == "tickets_lower"
        #             q21 = self.player.tickets_lower
        #             correct = 2250
        #
        #         if participant.vars['qs_order2'][9] == "germans_higher":
        #             q22 = self.player.germans_higher
        #         elif participant.vars['qs_order2'][9] == "temporary_higher":
        #             q22 = self.player.temporary_higher
        #         elif participant.vars['qs_order2'][9] == "commissioner_higher":
        #             q22 = self.player.commissioner_higher
        #         elif participant.vars['qs_order2'][9] == "age_higher":
        #             q22 = self.player.age_higher
        #         elif participant.vars['qs_order2'][9] == "allowance_higher":
        #             q22 = self.player.allowance_higher
        #         elif participant.vars['qs_order2'][9] == "paper_higher":
        #             q22 = self.player.paper_higher
        #         elif participant.vars['qs_order2'][9] == "printers_higher":
        #             q22 = self.player.printers_higher
        #         elif participant.vars['qs_order2'][9] == "laptops_higher":
        #             q22 = self.player.laptops_higher
        #         else:
        #             # participant.vars['qs_order2'][9] == "tickets_higher":
        #             q22 = self.player.tickets_higher
        #
        #         question1 = self.player.emails_lower
        #         question2 = self.player.emails_higher
        #         question3 = self.player.temporary_lower
        #         question4 = self.player.temporary_higher
        #         question5 = self.player.commissioner_lower
        #         question6 = self.player.commissioner_higher
        #         question7 = self.player.age_lower
        #         question8 = self.player.age_higher
        #         question9 = self.player.allowance_lower
        #         question10 = self.player.allowance_higher
        #         question11 = self.player.paper_lower
        #         question12 = self.player.paper_higher
        #         question13 = self.player.printers_lower
        #         question14 = self.player.printers_higher
        #         question15 = self.player.laptops_lower
        #         question16 = self.player.laptops_higher
        #         question17 = self.player.tickets_lower
        #         question18 = self.player.tickets_higher
        #         question19 = self.player.germans_lower
        #         question20 = self.player.germans_higher
        #
        #         if question1 == None:
        #             question1 = "(skipped)"
        #         if question2 == None:
        #             question2 = "(skipped)"
        #         if question3 == None:
        #             question3 = "(skipped)"
        #         if question4 == None:
        #             question4 = "(skipped)"
        #         if question5 == None:
        #             question5 = "(skipped)"
        #         if question6 == None:
        #             question6 = "(skipped)"
        #         if question7 == None:
        #             question7 = "(skipped)"
        #         if question8 == None:
        #             question8 = "(skipped)"
        #         if question9 == None:
        #             question9 = "(skipped)"
        #         if question10 == None:
        #             question10 = "(skipped)"
        #         if question11 == None:
        #             question11 = "(skipped)"
        #         if question12 == None:
        #             question12 = "(skipped)"
        #         if question13 == None:
        #             question13 = "(skipped)"
        #         if question14 == None:
        #             question14 = "(skipped)"
        #         if question15 == None:
        #             question15 = "(skipped)"
        #         if question16 == None:
        #             question16 = "(skipped)"
        #         if question17 == None:
        #             question17 = "(skipped)"
        #         if question18 == None:
        #             question18 = "(skipped)"
        #         if question19 == None:
        #             question19 = "(skipped)"
        #         if question20 == None:
        #             question20 = "(skipped)"
        #
        #         down = [question1, question3, question5, question7, question9, question11, question13, question15, question17,
        #                 question19]
        #         up = [question2, question4, question6, question8, question10, question12, question14, question16, question18,
        #               question20]
        #
        #         correct_answers = [53, 2700, 2340, 233, 59, 1418, 710, 3503, 9000, 2250]
        #         CORRECT = 0
        #         for i in range(0, len(correct_answers)):
        #             try:
        #                 if down[i] <= correct_answers[i] <= up[i]:
        #                     CORRECT += 1
        #             except:
        #                 continue
        #
        #         ANSWERED = 0
        #         for i in range(0, len(correct_answers)):
        #             try:
        #                 if down[i] >= 0 and up[i] >= 0:
        #                     ANSWERED += 1
        #                 elif down[i] >= 0 and up[i] == "(skipped)":
        #                     ANSWERED += 0
        #                 elif down[i] == "(skipped)" and up[i] >= 0:
        #                     ANSWERED += 0
        #                 else:
        #                     ANSWERED += 0
        #             except:
        #                 continue
        #
        #         CORRECT = round(CORRECT, 1)
        #         CORRECT_P = round(ANSWERED * 0.9, 1)
        try:
            PERCENT = round(100 * CORRECT / ANSWERED, 1)
        except:
            PERCENT = 0
        #
        #         return dict(
        #             CORRECT=CORRECT,
        #             CORRECT_P=CORRECT_P,
        #             ANSWERED=ANSWERED,
        #             q21=q21,
        #             q22=q22,
        #             correct=correct,
        #         )
        #
        # #unchanged
        # class Q12(Page):
        #     form_model = 'player'
        #
        #     def get_form_fields(self):
        #         participant = self.player.participant
        #         set11 = [participant.vars['qs_order'][10], participant.vars['qs_order2'][10], participant.vars['qs_order4'][10],
        #                  participant.vars['qs_order3'][10],
        #                  'skip_all']
        #         return set11
        #
        #     def is_displayed(self):
        #         if self.player.skip_all == True:
        #             return True
        #
        #     def error_message(self, values):
        #         participant = self.player.participant
        #         q1 = participant.vars['qs_order'][11]
        #         q2 = participant.vars['qs_order2'][11]
        #         print('values is', values)
        #         try:
        #             if values[participant.vars['qs_order'][11]] >= values[participant.vars['qs_order2'][11]]:
        #                 return "When you claim that the number we asked about is between A and B, please make sure that your B is larger than A."
        #         except:
        #             pass
        #
        #
        # class Q12feedback(Page):
        #     form_model = 'player'
        #
        #     def is_displayed(self):
        #         participant = self.player.participant
        #         if participant.vars['qs_order'][11] == "germans_lower":
        #             q23 = self.player.germans_lower
        #         elif participant.vars['qs_order'][11] == "temporary_lower":
        #             q23 = self.player.temporary_lower
        #         elif participant.vars['qs_order'][11] == "commissioner_lower":
        #             q23 = self.player.commissioner_lower
        #         elif participant.vars['qs_order'][11] == "age_lower":
        #             q23 = self.player.age_lower
        #         elif participant.vars['qs_order'][11] == "allowance_lower":
        #             q23 = self.player.allowance_lower
        #         elif participant.vars['qs_order'][11] == "cited_lower":
        #             q23 = self.player.cited_lower
        #         elif participant.vars['qs_order'][11] == "paper_lower":
        #             q23 = self.player.paper_lower
        #         elif participant.vars['qs_order'][11] == "printers_lower":
        #             q23 = self.player.printers_lower
        #         elif participant.vars['qs_order'][11] == "driving_lower":
        #             q23 = self.player.driving_lower
        #         elif participant.vars['qs_order'][11] == "emissions_lower":
        #             q23 = self.player.emissions_lower
        #         elif participant.vars['qs_order'][11] == "emails_lower":
        #             q23 = self.player.emails_lower
        #         elif participant.vars['qs_order'][11] == "laptops_lower":
        #             q23 = self.player.laptops_lower
        #         else:
        #             # participant.vars['qs_order'][11] == "tickets_lower"
        #             q23 = self.player.tickets_lower
        #
        #         if participant.vars['qs_order2'][11] == "germans_higher":
        #             q24 = self.player.germans_higher
        #         elif participant.vars['qs_order2'][11] == "temporary_higher":
        #             q24 = self.player.temporary_higher
        #         elif participant.vars['qs_order2'][11] == "commissioner_higher":
        #             q24 = self.player.commissioner_higher
        #         elif participant.vars['qs_order2'][11] == "age_higher":
        #             q24 = self.player.age_higher
        #         elif participant.vars['qs_order2'][11] == "allowance_higher":
        #             q24 = self.player.allowance_higher
        #         elif participant.vars['qs_order2'][11] == "cited_higher":
        #             q24 = self.player.cited_higher
        #         elif participant.vars['qs_order2'][11] == "paper_higher":
        #             q24 = self.player.paper_higher
        #         elif participant.vars['qs_order2'][11] == "printers_higher":
        #             q24 = self.player.printers_higher
        #         elif participant.vars['qs_order2'][11] == "driving_higher":
        #             q24 = self.player.driving_higher
        #         elif participant.vars['qs_order2'][11] == "emissions_higher":
        #             q24 = self.player.emissions_higher
        #         elif participant.vars['qs_order2'][11] == "emails_higher":
        #             q24 = self.player.emails_higher
        #         elif participant.vars['qs_order2'][11] == "laptops_higher":
        #             q24 = self.player.laptops_higher
        #         else:
        #             # participant.vars['qs_order2'][11] == "tickets_higher":
        #             q24 = self.player.tickets_higher
        #
        #         if q23 is not None and q24 is not None:
        #             return True
        #
        #     def vars_for_template(self):
        #         participant = self.player.participant
        #         if participant.vars['qs_order'][9] == "germans_lower":
        #             q23 = self.player.germans_lower
        #             correct = 2700
        #         elif participant.vars['qs_order'][9] == "temporary_lower":
        #             q23 = self.player.temporary_lower
        #             correct = 2340
        #         elif participant.vars['qs_order'][9] == "commissioner_lower":
        #             q23 = self.player.commissioner_lower
        #             correct = 233
        #         elif participant.vars['qs_order'][9] == "age_lower":
        #             q23 = self.player.age_lower
        #             correct = 59
        #         elif participant.vars['qs_order'][9] == "allowance_lower":
        #             q23 = self.player.allowance_lower
        #             correct = 1418
        #         elif participant.vars['qs_order'][9] == "cited_lower":
        #             q23 = self.player.cited_lower
        #             correct = 86
        #         elif participant.vars['qs_order'][9] == "paper_lower":
        #             q23 = self.player.paper_lower
        #             correct = 710
        #         elif participant.vars['qs_order'][9] == "printers_lower":
        #             q23 = self.player.printers_lower
        #             correct = 3503
        #         elif participant.vars['qs_order'][9] == "driving_lower":
        #             q23 = self.player.driving_lower
        #             correct = 1432
        #         elif participant.vars['qs_order'][9] == "emissions_lower":
        #             q23 = self.player.emissions_lower
        #             correct = 10555
        #         elif participant.vars['qs_order'][9] == "emails_lower":
        #             q23 = self.player.emails_lower
        #             correct = 53
        #         elif participant.vars['qs_order'][9] == "laptops_lower":
        #             q23 = self.player.laptops_lower
        #             correct = 9000
        #         else:
        #             # participant.vars['qs_order'][9] == "tickets_lower"
        #             q23 = self.player.tickets_lower
        #             correct = 2250
        #
        #         if participant.vars['qs_order2'][11] == "germans_higher":
        #             q24 = self.player.germans_higher
        #         elif participant.vars['qs_order2'][11] == "temporary_higher":
        #             q24 = self.player.temporary_higher
        #         elif participant.vars['qs_order2'][11] == "commissioner_higher":
        #             q24 = self.player.commissioner_higher
        #         elif participant.vars['qs_order2'][11] == "age_higher":
        #             q24 = self.player.age_higher
        #         elif participant.vars['qs_order2'][11] == "allowance_higher":
        #             q24 = self.player.allowance_higher
        #         elif participant.vars['qs_order2'][11] == "cited_higher":
        #             q24 = self.player.cited_higher
        #         elif participant.vars['qs_order2'][11] == "paper_higher":
        #             q24 = self.player.paper_higher
        #         elif participant.vars['qs_order2'][11] == "printers_higher":
        #             q24 = self.player.printers_higher
        #         elif participant.vars['qs_order2'][11] == "driving_higher":
        #             q24 = self.player.driving_higher
        #         elif participant.vars['qs_order2'][11] == "emissions_higher":
        #             q24 = self.player.emissions_higher
        #         elif participant.vars['qs_order2'][11] == "emails_higher":
        #             q24 = self.player.emails_higher
        #         elif participant.vars['qs_order2'][11] == "laptops_higher":
        #             q24 = self.player.laptops_higher
        #         else:
        #             # participant.vars['qs_order2'][11] == "tickets_higher":
        #             q24 = self.player.tickets_higher
        #
        #         question1 = self.player.germans_lower
        #         question2 = self.player.germans_higher
        #         question3 = self.player.temporary_lower
        #         question4 = self.player.temporary_higher
        #         question5 = self.player.commissioner_lower
        #         question6 = self.player.commissioner_higher
        #         question7 = self.player.age_lower
        #         question8 = self.player.age_higher
        #         question9 = self.player.allowance_lower
        #         question10 = self.player.allowance_higher
        #         question11 = self.player.cited_lower
        #         question12 = self.player.cited_higher
        #         question13 = self.player.paper_lower
        #         question14 = self.player.paper_higher
        #         question15 = self.player.printers_lower
        #         question16 = self.player.printers_higher
        #         question17 = self.player.driving_lower
        #         question18 = self.player.driving_higher
        #         question19 = self.player.emissions_lower
        #         question20 = self.player.emissions_higher
        #         question21 = self.player.emails_lower
        #         question22 = self.player.emails_higher
        #         question23 = self.player.laptops_lower
        #         question24 = self.player.laptops_higher
        #         question25 = self.player.tickets_lower
        #         question26 = self.player.tickets_higher
        #
        #         if question1 == None:
        #             question1 = "(skipped)"
        #         if question2 == None:
        #             question2 = "(skipped)"
        #         if question3 == None:
        #             question3 = "(skipped)"
        #         if question4 == None:
        #             question4 = "(skipped)"
        #         if question5 == None:
        #             question5 = "(skipped)"
        #         if question6 == None:
        #             question6 = "(skipped)"
        #         if question7 == None:
        #             question7 = "(skipped)"
        #         if question8 == None:
        #             question8 = "(skipped)"
        #         if question9 == None:
        #             question9 = "(skipped)"
        #         if question10 == None:
        #             question10 = "(skipped)"
        #         if question11 == None:
        #             question11 = "(skipped)"
        #         if question12 == None:
        #             question12 = "(skipped)"
        #         if question13 == None:
        #             question13 = "(skipped)"
        #         if question14 == None:
        #             question14 = "(skipped)"
        #         if question15 == None:
        #             question15 = "(skipped)"
        #         if question16 == None:
        #             question16 = "(skipped)"
        #         if question17 == None:
        #             question17 = "(skipped)"
        #         if question18 == None:
        #             question18 = "(skipped)"
        #         if question19 == None:
        #             question19 = "(skipped)"
        #         if question20 == None:
        #             question20 = "(skipped)"
        #         if question21 == None:
        #             question21 = "(skipped)"
        #         if question22 == None:
        #             question22 = "(skipped)"
        #         if question23 == None:
        #             question23 = "(skipped)"
        #         if question24 == None:
        #             question24 = "(skipped)"
        #         if question25 == None:
        #             question25 = "(skipped)"
        #         if question26 == None:
        #             question26 = "(skipped)"
        #
        #         down = [question1, question3, question5, question7, question9, question11, question13, question15, question17,
        #                 question19, question21, question23, question25]
        #         up = [question2, question4, question6, question8, question10, question12, question14, question16, question18,
        #               question20, question22, question24, question26]
        #
        #         correct_answers = [2700, 2340, 233, 59, 1418, 86, 710, 3503, 1432, 10555, 53, 9000, 2250]
        #         CORRECT = 0
        #         for i in range(0, len(correct_answers)):
        #             try:
        #                 if down[i] <= correct_answers[i] and up[i] >= correct_answers[i]:
        #                     CORRECT += 1
        #             except:
        #                 continue
        #
        #         ANSWERED = 0
        #         for i in range(0, len(correct_answers)):
        #             try:
        #                 if down[i] >= 0 and up[i] >= 0:
        #                     ANSWERED += 1
        #                 elif down[i] >= 0 and up[i] == "(skipped)":
        #                     ANSWERED += 0
        #                 elif down[i] == "(skipped)" and up[i] >= 0:
        #                     ANSWERED += 0
        #                 else:
        #                     ANSWERED += 0
        #             except:
        #                 continue
        #
        #         CORRECT = round(CORRECT, 1)
        #         CORRECT_P = round(ANSWERED * 0.9, 1)
        try:
            PERCENT = round(100 * CORRECT / ANSWERED, 1)
        except:
            PERCENT = 0


#
#         return dict(
#             CORRECT=CORRECT,
#             CORRECT_P=CORRECT_P,
#             ANSWERED=ANSWERED,
#             q23=q23,
#             q24=q24,
#             correct=correct,
#         )
#
#
# class Q13(Page):
#     form_model = 'player'
#
#     def get_form_fields(self):
#         participant = self.player.participant
#         set12 = [participant.vars['qs_order'][11], participant.vars['qs_order2'][11], participant.vars['qs_order4'][11],
#                  participant.vars['qs_order3'][11],
#                  'skip_all']
#         return set12
#
#     def is_displayed(self):
#         if self.player.skip_all == True:
#             return True
#
#     def error_message(self, values):
#         participant = self.player.participant
#         q1 = participant.vars['qs_order'][12]
#         q2 = participant.vars['qs_order2'][12]
#         print('values is', values)
#         try:
#             if values[participant.vars['qs_order'][12]] >= values[participant.vars['qs_order2'][12]]:
#                 return "When you claim that the number we asked about is between A and B, please make sure that your B is larger than A."
#         except:
#             pass
#
#
# class Q13feedback(Page):
#     form_model = 'player'
#
#     def is_displayed(self):
#         participant = self.player.participant
#         if participant.vars['qs_order'][12] == "germans_lower":
#             q25 = self.player.germans_lower
#         elif participant.vars['qs_order'][12] == "temporary_lower":
#             q25 = self.player.temporary_lower
#         elif participant.vars['qs_order'][12] == "commissioner_lower":
#             q25 = self.player.commissioner_lower
#         elif participant.vars['qs_order'][12] == "age_lower":
#             q25 = self.player.age_lower
#         elif participant.vars['qs_order'][12] == "allowance_lower":
#             q25 = self.player.allowance_lower
#         elif participant.vars['qs_order'][12] == "cited_lower":
#             q25 = self.player.cited_lower
#         elif participant.vars['qs_order'][12] == "paper_lower":
#             q25 = self.player.paper_lower
#         elif participant.vars['qs_order'][12] == "printers_lower":
#             q25 = self.player.printers_lower
#         elif participant.vars['qs_order'][12] == "driving_lower":
#             q25 = self.player.driving_lower
#         elif participant.vars['qs_order'][12] == "emissions_lower":
#             q25 = self.player.emissions_lower
#         elif participant.vars['qs_order'][12] == "emails_lower":
#             q25 = self.player.emails_lower
#         elif participant.vars['qs_order'][12] == "laptops_lower":
#             q25 = self.player.laptops_lower
#         else:
#             # participant.vars['qs_order'][12] == "tickets_lower"
#             q25 = self.player.tickets_lower
#
#         if participant.vars['qs_order2'][12] == "germans_higher":
#             q26 = self.player.germans_higher
#         elif participant.vars['qs_order2'][12] == "temporary_higher":
#             q26 = self.player.temporary_higher
#         elif participant.vars['qs_order2'][12] == "commissioner_higher":
#             q26 = self.player.commissioner_higher
#         elif participant.vars['qs_order2'][12] == "age_higher":
#             q26 = self.player.age_higher
#         elif participant.vars['qs_order2'][12] == "allowance_higher":
#             q26 = self.player.allowance_higher
#         elif participant.vars['qs_order2'][12] == "cited_higher":
#             q26 = self.player.cited_higher
#         elif participant.vars['qs_order2'][12] == "paper_higher":
#             q26 = self.player.paper_higher
#         elif participant.vars['qs_order2'][12] == "printers_higher":
#             q26 = self.player.printers_higher
#         elif participant.vars['qs_order2'][12] == "driving_higher":
#             q26 = self.player.driving_higher
#         elif participant.vars['qs_order2'][12] == "emissions_higher":
#             q26 = self.player.emissions_higher
#         elif participant.vars['qs_order2'][12] == "emails_higher":
#             q26 = self.player.emails_higher
#         elif participant.vars['qs_order2'][12] == "laptops_higher":
#             q26 = self.player.laptops_higher
#         else:
#             # participant.vars['qs_order2'][12] == "tickets_higher":
#             q26 = self.player.tickets_higher
#
#         if q25 is not None and q26 is not None:
#             return True
#
#     def vars_for_template(self):
#         participant = self.player.participant
#         if participant.vars['qs_order'][12] == "germans_lower":
#             q25 = self.player.germans_lower
#             correct = 2700
#         elif participant.vars['qs_order'][12] == "temporary_lower":
#             q25 = self.player.temporary_lower
#             correct = 2340
#         elif participant.vars['qs_order'][12] == "commissioner_lower":
#             q25 = self.player.commissioner_lower
#             correct = 233
#         elif participant.vars['qs_order'][12] == "age_lower":
#             q25 = self.player.age_lower
#             correct = 59
#         elif participant.vars['qs_order'][12] == "allowance_lower":
#             q25 = self.player.allowance_lower
#             correct = 1418
#         elif participant.vars['qs_order'][12] == "cited_lower":
#             q25 = self.player.cited_lower
#             correct = 86
#         elif participant.vars['qs_order'][12] == "paper_lower":
#             q25 = self.player.paper_lower
#             correct = 710
#         elif participant.vars['qs_order'][12] == "printers_lower":
#             q25 = self.player.printers_lower
#             correct = 3503
#         elif participant.vars['qs_order'][12] == "driving_lower":
#             q25 = self.player.driving_lower
#             correct = 1432
#         elif participant.vars['qs_order'][12] == "emissions_lower":
#             q25 = self.player.emissions_lower
#             correct = 10555
#         elif participant.vars['qs_order'][12] == "emails_lower":
#             q25 = self.player.emails_lower
#             correct = 53
#         elif participant.vars['qs_order'][12] == "laptops_lower":
#             q25 = self.player.laptops_lower
#             correct = 9000
#         else:
#             # participant.vars['qs_order'][12] == "tickets_lower"
#             q25 = self.player.tickets_lower
#             correct = 2250
#
#         if participant.vars['qs_order2'][12] == "germans_higher":
#             q26 = self.player.germans_higher
#         elif participant.vars['qs_order2'][12] == "temporary_higher":
#             q26 = self.player.temporary_higher
#         elif participant.vars['qs_order2'][12] == "commissioner_higher":
#             q26 = self.player.commissioner_higher
#         elif participant.vars['qs_order2'][12] == "age_higher":
#             q26 = self.player.age_higher
#         elif participant.vars['qs_order2'][12] == "allowance_higher":
#             q26 = self.player.allowance_higher
#         elif participant.vars['qs_order2'][12] == "cited_higher":
#             q26 = self.player.cited_higher
#         elif participant.vars['qs_order2'][12] == "paper_higher":
#             q26 = self.player.paper_higher
#         elif participant.vars['qs_order2'][12] == "printers_higher":
#             q26 = self.player.printers_higher
#         elif participant.vars['qs_order2'][12] == "driving_higher":
#             q26 = self.player.driving_higher
#         elif participant.vars['qs_order2'][12] == "emissions_higher":
#             q26 = self.player.emissions_higher
#         elif participant.vars['qs_order2'][12] == "emails_higher":
#             q26 = self.player.emails_higher
#         elif participant.vars['qs_order2'][12] == "laptops_higher":
#             q26 = self.player.laptops_higher
#         else:
#             # participant.vars['qs_order2'][12] == "tickets_higher":
#             q26 = self.player.tickets_higher
#
#         if q25 is None:
#             q25 = "(skipped)"
#         if q26 is None:
#             q26 = "(skipped)"
#
#         return dict(
#             q25=q25,
#             q26=q26,
#             correct=correct,
#         )


class Assumed_success(Page):
    form_model = 'player'
    form_fields = ['assumed']

    def vars_for_template(self):
        q1 = self.player.emails_lower
        q2 = self.player.emails_higher
        q3 = self.player.temporary_lower
        q4 = self.player.temporary_higher
        q5 = self.player.commissioner_lower
        q6 = self.player.commissioner_higher
        q7 = self.player.age_lower
        q8 = self.player.age_higher
        q9 = self.player.allowance_lower
        q10 = self.player.allowance_higher
        q11 = self.player.paper_lower
        q12 = self.player.paper_higher
        q13 = self.player.printers_lower
        q14 = self.player.printers_higher
        q15 = self.player.laptops_lower
        q16 = self.player.laptops_higher
        q17 = self.player.tickets_lower
        q18 = self.player.tickets_higher
        q19 = self.player.germans_lower
        q20 = self.player.germans_higher

        if q1 == None:
            q1 = "(skipped)"
        if q2 == None:
            q2 = "(skipped)"
        if q3 == None:
            q3 = "(skipped)"
        if q4 == None:
            q4 = "(skipped)"
        if q5 == None:
            q5 = "(skipped)"
        if q6 == None:
            q6 = "(skipped)"
        if q7 == None:
            q7 = "(skipped)"
        if q8 == None:
            q8 = "(skipped)"
        if q9 == None:
            q9 = "(skipped)"
        if q10 == None:
            q10 = "(skipped)"
        if q11 == None:
            q11 = "(skipped)"
        if q12 == None:
            q12 = "(skipped)"
        if q13 == None:
            q13 = "(skipped)"
        if q14 == None:
            q14 = "(skipped)"
        if q15 == None:
            q15 = "(skipped)"
        if q16 == None:
            q16 = "(skipped)"
        if q17 == None:
            q17 = "(skipped)"
        if q18 == None:
            q18 = "(skipped)"
        if q19 == None:
            q19 = "(skipped)"
        if q20 == None:
            q20 = "(skipped)"

        down = [q1, q3, q5, q7, q9, q11, q13, q15, q17, q19]
        up = [q2, q4, q6, q8, q10, q12, q14, q16, q18, q20]

        ANSWERED = 0
        for i in range(0, len(down)):
            try:
                if down[i] >= 0 and up[i] >= 0:
                    ANSWERED += 1
                elif down[i] >= 0 and up[i] == "(skipped)":
                    ANSWERED += 0
                elif down[i] == "(skipped)" and up[i] >= 0:
                    ANSWERED += 0
                else:
                    ANSWERED += 0
            except:
                continue

        return dict(
            ANSWERED=ANSWERED,
            q1=q1,
            q2=q2,
            q3=q3,
            q4=q4,
            q5=q5,
            q6=q6,
            q7=q7,
            q8=q8,
            q9=q9,
            q10=q10,
            q11=q11,
            q12=q12,
            q13=q13,
            q14=q14,
            q15=q15,
            q16=q16,
            q17=q17,
            q18=q18,
            q19=q19,
            q20=q20,
        )

    def error_message(self, values):
        q1 = self.player.emails_lower
        q2 = self.player.emails_higher
        q3 = self.player.temporary_lower
        q4 = self.player.temporary_higher
        q5 = self.player.commissioner_lower
        q6 = self.player.commissioner_higher
        q7 = self.player.age_lower
        q8 = self.player.age_higher
        q9 = self.player.allowance_lower
        q10 = self.player.allowance_higher
        q11 = self.player.paper_lower
        q12 = self.player.paper_higher
        q13 = self.player.printers_lower
        q14 = self.player.printers_higher
        q15 = self.player.laptops_lower
        q16 = self.player.laptops_higher
        q17 = self.player.tickets_lower
        q18 = self.player.tickets_higher
        q19 = self.player.germans_lower
        q20 = self.player.germans_higher

        if q1 == None:
            q1 = "(skipped)"
        if q2 == None:
            q2 = "(skipped)"
        if q3 == None:
            q3 = "(skipped)"
        if q4 == None:
            q4 = "(skipped)"
        if q5 == None:
            q5 = "(skipped)"
        if q6 == None:
            q6 = "(skipped)"
        if q7 == None:
            q7 = "(skipped)"
        if q8 == None:
            q8 = "(skipped)"
        if q9 == None:
            q9 = "(skipped)"
        if q10 == None:
            q10 = "(skipped)"
        if q11 == None:
            q11 = "(skipped)"
        if q12 == None:
            q12 = "(skipped)"
        if q13 == None:
            q13 = "(skipped)"
        if q14 == None:
            q14 = "(skipped)"
        if q15 == None:
            q15 = "(skipped)"
        if q16 == None:
            q16 = "(skipped)"
        if q17 == None:
            q17 = "(skipped)"
        if q18 == None:
            q18 = "(skipped)"
        if q19 == None:
            q19 = "(skipped)"
        if q20 == None:
            q20 = "(skipped)"

        down = [q1, q3, q5, q7, q9, q11, q13, q15, q17, q19]
        up = [q2, q4, q6, q8, q10, q12, q14, q16, q18, q20]

        ANSWERED = 0
        for i in range(0, len(down)):
            try:
                if down[i] >= 0 and up[i] >= 0:
                    ANSWERED += 1
                elif down[i] >= 0 and up[i] == "(skipped)":
                    ANSWERED += 0
                elif down[i] == "(skipped)" and up[i] >= 0:
                    ANSWERED += 0
                else:
                    ANSWERED += 0
            except:
                continue
        print('values is', values)
        try:
            if values["assumed"] > ANSWERED:
                return "Please choose a number equal to or smaller than the number of the questions you answered."
        except:
            pass


class Real_success_treatment(Page):
    form_model = 'player'

    def is_displayed(self):
        if self.player.participant.vars['feedback'][0] == "feedback":
            return True

    def vars_for_template(self):
        q1 = self.player.emails_lower
        q2 = self.player.emails_higher
        q3 = self.player.temporary_lower
        q4 = self.player.temporary_higher
        q5 = self.player.commissioner_lower
        q6 = self.player.commissioner_higher
        q7 = self.player.age_lower
        q8 = self.player.age_higher
        q9 = self.player.allowance_lower
        q10 = self.player.allowance_higher
        q11 = self.player.paper_lower
        q12 = self.player.paper_higher
        q13 = self.player.printers_lower
        q14 = self.player.printers_higher
        q15 = self.player.laptops_lower
        q16 = self.player.laptops_higher
        q17 = self.player.tickets_lower
        q18 = self.player.tickets_higher
        q19 = self.player.germans_lower
        q20 = self.player.germans_higher

        if q1 == None:
            q1 = "(skipped)"
        if q2 == None:
            q2 = "(skipped)"
        if q3 == None:
            q3 = "(skipped)"
        if q4 == None:
            q4 = "(skipped)"
        if q5 == None:
            q5 = "(skipped)"
        if q6 == None:
            q6 = "(skipped)"
        if q7 == None:
            q7 = "(skipped)"
        if q8 == None:
            q8 = "(skipped)"
        if q9 == None:
            q9 = "(skipped)"
        if q10 == None:
            q10 = "(skipped)"
        if q11 == None:
            q11 = "(skipped)"
        if q12 == None:
            q12 = "(skipped)"
        if q13 == None:
            q13 = "(skipped)"
        if q14 == None:
            q14 = "(skipped)"
        if q15 == None:
            q15 = "(skipped)"
        if q16 == None:
            q16 = "(skipped)"
        if q17 == None:
            q17 = "(skipped)"
        if q18 == None:
            q18 = "(skipped)"
        if q19 == None:
            q19 = "(skipped)"
        if q20 == None:
            q20 = "(skipped)"

        down = [q1, q3, q5, q7, q9, q11, q13, q15, q17, q19]
        up = [q2, q4, q6, q8, q10, q12, q14, q16, q18, q20]

        correct = [53, 2340, 233, 59, 1418, 710, 3503, 9000, 2250, 2700]
        CORRECT = 0
        for i in range(0, len(correct)):
            try:
                if down[i] <= correct[i] and up[i] >= correct[i]:
                    CORRECT += 1
            except:
                continue

        ANSWERED = 0
        for i in range(0, len(correct)):
            try:
                if down[i] >= 0 and up[i] >= 0:
                    ANSWERED += 1
                elif down[i] >= 0 and up[i] == "(skipped)":
                    ANSWERED += 0
                elif down[i] == "(skipped)" and up[i] >= 0:
                    ANSWERED += 0
                else:
                    ANSWERED += 0
            except:
                continue

        CORRECT_P = round(ANSWERED * 0.9, 1)

        return dict(
            CORRECT=CORRECT,
            CORRECT_P=CORRECT_P,
            ANSWERED=ANSWERED,
        )


class Real_success(Page):
    form_model = 'player'

    def is_displayed(self):
        if self.player.participant.vars['feedback'][0] == "no_feedback":
            return True

    def vars_for_template(self):
        q1 = self.player.emails_lower
        q2 = self.player.emails_higher
        q3 = self.player.temporary_lower
        q4 = self.player.temporary_higher
        q5 = self.player.commissioner_lower
        q6 = self.player.commissioner_higher
        q7 = self.player.age_lower
        q8 = self.player.age_higher
        q9 = self.player.allowance_lower
        q10 = self.player.allowance_higher
        q11 = self.player.paper_lower
        q12 = self.player.paper_higher
        q13 = self.player.printers_lower
        q14 = self.player.printers_higher
        q15 = self.player.laptops_lower
        q16 = self.player.laptops_higher
        q17 = self.player.tickets_lower
        q18 = self.player.tickets_higher
        q19 = self.player.germans_lower
        q20 = self.player.germans_higher

        if q1 == None:
            q1 = "(skipped)"
        if q2 == None:
            q2 = "(skipped)"
        if q3 == None:
            q3 = "(skipped)"
        if q4 == None:
            q4 = "(skipped)"
        if q5 == None:
            q5 = "(skipped)"
        if q6 == None:
            q6 = "(skipped)"
        if q7 == None:
            q7 = "(skipped)"
        if q8 == None:
            q8 = "(skipped)"
        if q9 == None:
            q9 = "(skipped)"
        if q10 == None:
            q10 = "(skipped)"
        if q11 == None:
            q11 = "(skipped)"
        if q12 == None:
            q12 = "(skipped)"
        if q13 == None:
            q13 = "(skipped)"
        if q14 == None:
            q14 = "(skipped)"
        if q15 == None:
            q15 = "(skipped)"
        if q16 == None:
            q16 = "(skipped)"
        if q17 == None:
            q17 = "(skipped)"
        if q18 == None:
            q18 = "(skipped)"
        if q19 == None:
            q19 = "(skipped)"
        if q20 == None:
            q20 = "(skipped)"

        down = [q1, q3, q5, q7, q9, q11, q13, q15, q17, q19]
        up = [q2, q4, q6, q8, q10, q12, q14, q16, q18, q20]

        correct = [53, 2340, 233, 59, 1418, 710, 3503, 9000, 2250, 2700]
        CORRECT = 0
        for i in range(0, len(correct)):
            try:
                if down[i] <= correct[i] and up[i] >= correct[i]:
                    CORRECT += 1
            except:
                continue

        ANSWERED = 0
        for i in range(0, len(correct)):
            try:
                if down[i] >= 0 and up[i] >= 0:
                    ANSWERED += 1
                elif down[i] >= 0 and up[i] == "(skipped)":
                    ANSWERED += 0
                elif down[i] == "(skipped)" and up[i] >= 0:
                    ANSWERED += 0
                else:
                    ANSWERED += 0
            except:
                continue

        CORRECT_P = round(ANSWERED * 0.9, 1)

        return dict(
            CORRECT=CORRECT,
            CORRECT_P=CORRECT_P,
            ANSWERED=ANSWERED,
            q1=q1,
            q2=q2,
            q3=q3,
            q4=q4,
            q5=q5,
            q6=q6,
            q7=q7,
            q8=q8,
            q9=q9,
            q10=q10,
            q11=q11,
            q12=q12,
            q13=q13,
            q14=q14,
            q15=q15,
            q16=q16,
            q17=q17,
            q18=q18,
            q19=q19,
            q20=q20,
        )


class About(Page):
    form_model = 'player'
    form_fields = ['final']

    def is_displayed(self):
        return True


class Thanks(Page):
    form_model = 'player'
    form_fields = ['feedback_on']


# treatment:
page_sequence = [Welcome, Q1, Q1feedback, Q2, Q2feedback, Q3, Q3feedback, Q4, Q4feedback, Q5, Q5feedback, Q6,
                 Q6feedback,
                 Q7, Q7feedback, Q8, Q8feedback, Q9, Q9feedback, Q10, Q10feedback, Assumed_success, Real_success,
                 Real_success_treatment, About,
                 Thanks]

# no treatment:
# page_sequence = [Welcome, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Assumed_success, Real_success, About, Thanks]
