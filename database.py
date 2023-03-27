from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

engine = create_engine('sqlite:///data.db', echo=False)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    group = Column(Integer, nullable=False)
    correct_answers = Column(Integer, nullable=True)
    done = Column(Integer, nullable=True)
    date = Column(DateTime, nullable=False)


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    queston_main = Column(String(800), nullable=False)
    answer1 = Column(String(800), nullable=True)
    answer2 = Column(String(800), nullable=True)
    answer3 = Column(String(800), nullable=True)
    answer4 = Column(String(800), nullable=True)
    question_photo = Column(String(800), default=0)
    correct_answer = Column(String(800), nullable=False)


# class UserAnswer(Base):
#     __tablename__ = 'users_answers'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     user_question = Column(String(880), ForeignKey('questions.id'))
#     user_answer = Column(String(880))
#     correctness = Column(Integer)

class UserAnswer1(Base):
    __tablename__ = 'users_answers2'
    id = Column(Integer, primary_key=True)
    name = Column(String(880))
    user_answer = Column(String(880))
#
#
# class SubscribtionPeriod(Base):
#     __tablename__ = 'subscribtion_period'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(String(880), ForeignKey('users.id'))
#     start_date = Column(DateTime, nullable=False)
#     end_date = Column(DateTime, nullable=False)




# Create all tables in the engine. This is equivalent to "Create Table"
# Base.metadata.create_all(engine)