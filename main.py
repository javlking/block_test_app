import random

from fastapi import FastAPI, Request, Form, Body, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse
from threading import Thread

# import telebot
from pydantic import BaseModel
from typing import Optional, List, Dict
import utils

# bot = telebot.TeleBot('5105426169:AAHR0FcfZwgCEeDj_wskbAkbvwUKLLnpxaU', parse_mode='HTML')
# Create a model of student
# class Student(BaseModel):
#     name: Optional[str]
#     group: Optional[int] = 30
#     answers: Optional[List[Dict[str, str]]]
#     score: Optional[int]


# Create an object of api
app = FastAPI()

# Template attribute
template = Jinja2Templates(directory='templates')


def send_tg(name, sold):
    creative = ''
    for i in sold[24:]:
        if not i:
            creative += f'Нет ответа\n'
        else:
            creative += f'{i}\n'

    i = random.choice([295612129, 791555605])
    bot.send_message(int(i), text=f'<b>Ученик:</b> {name}\n\n<b>Закрытые:</b> \n{creative}')


# Main page
@app.get('/')
def index(request: Request):

    return template.TemplateResponse('index.html', {'request': request})


# Register student and start test
@app.post('/start_test', response_class=RedirectResponse)
def start_test(name: str = Form(...), group: int = Form(...)):
    utils.register_user(name, group)

    return RedirectResponse(url=f'/test_time/{name}', status_code=302)


@app.get('/test_time/{name}')
def test_time(request: Request, name: Optional[str]):
    questions = utils.get_questions()

    return template.TemplateResponse('start_test.html', {'request': request, 'questions': questions, 'name': name})


# Passed test
@app.post('/done/{name}')
def test_passed(name: Optional[str], request: Request, form_data=Body(...)):
    my_string = form_data.decode('utf-8')
    key_value_pairs = my_string.split('&')
    tuples = [pair.split('=') for pair in key_value_pairs]
    answers = dict(tuples)

    user_stat = utils.set_answer(name, answers)

    questions = utils.get_questions()
    print(user_stat[2])
    # print(name, count)
    return template.TemplateResponse('answer.html', {'request': request,
                                                     'questions': questions[:31],
                                                     'answers': user_stat[0],
                                                     'user_answers': user_stat[1],
                                                     'user_answer': user_stat[2]})

    # return RedirectResponse(url=f'/done/{name}/{user_stat[0]}', status_code=302)


@app.get('/done/{name}/{count}', response_class=HTMLResponse)
def test_passed(request: Request, count: int):
    questions = utils.get_questions()
    # print(name, count)
    return template.TemplateResponse('answer.html', {'request': request, 'questions': questions[:31], 'answers': count})




