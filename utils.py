import database
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from datetime import datetime

from threading import Thread


def get_questions():
    engine = create_engine('sqlite:///data.db', echo=True, connect_args={'check_same_thread': False})
    session = Session(bind=engine)

    questions = session.query(database.Question).all()

    m = []
    for question in questions:
        p = dict(id=str(question.id),
                 question_text=question.queston_main,
                 answer_1=question.answer1,
                 answer_2=question.answer2,
                 answer_3=question.answer3,
                 answer_4=question.answer4,
                 correct_answer=question.correct_answer)
        m.append(p)

    return m


# Register user
def register_user(name, group):
    engine = create_engine('sqlite:///data.db', echo=True, connect_args={'check_same_thread': False})
    session = Session(bind=engine)
    user = session.query(database.User).filter_by(name=name).first()
    if not user:
        user = database.User(name=name, group=group, done=1, date=datetime.now(), correct_answers=0)
        session.add(user)
        session.commit()


# Set questions
def check_question(db_answers, user_answers):
    counter = 1
    corrects = 0
    stat = {'corrects': {}, 'incorrect': {}}

    while counter < 31:
        if db_answers.get(str(counter)) == user_answers.get(str(counter)):
            stat['corrects'][counter] = user_answers.get(str(counter))
            corrects += 1

        else:
            stat['incorrect'][counter] = user_answers.get(str(counter))

        counter += 1

    return corrects, stat, user_answers


def set_answer(name, user_answers):
    engine = create_engine('sqlite:///data.db', echo=True, connect_args={'check_same_thread': False})
    session = Session(bind=engine)

    questions = session.query(database.Question).all()
    database_answers = {}
    for question in questions:
        database_answers[str(question.id)] = str(question.correct_answer)

    return check_question(database_answers, user_answers)


# # Check for the correctness
# def check_answer(answer):
#     engine = create_engine('sqlite:///data.db', echo=True, connect_args={'check_same_thread': False})
#     session = Session(bind=engine)
#     for i in answer:
#         get_answer = session.query(database.Question).all()
#     m = 0
#
#
#     return m