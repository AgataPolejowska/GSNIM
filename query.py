from website import db
from website.models import Respondent, Question, Option, Answer


# TESTING QUERIES

# questions = Question.query.all()
# print(questions[0].text)

# options = Option.query.all()
# print(options)

# options_objects_list = Option.query.all()
# options_1_question = []

# for option in options_objects_list:
#     print(option.question_id)
#     #if option.question_assigned == id - 1:
#     #    options_1_question.append(option.option_text)

# respondents = Respondent.query.all()
# women_count = 0
# men_count = 0

# for respondent in respondents:
#     if respondent.gender == 1:
#         women_count = women_count + 1
#     if respondent.gender == 2:
#         men_count = men_count + 1

# print(women_count, men_count)


questions = Question.query.all()
answers = Answer.query.all()

question_list = []
answer_list = []

for answer in answers:
    if answer.respondent_id == respondent_id:
        question_list.append(answer.question_assigned)
        answer_list.append(answer)