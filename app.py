import os
from os.path import join, dirname

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, dotenv_values

from posts.blueprint import posts
from telegram.handler import handler, dp

from aiogram.utils import executor



app = Flask(__name__)
load_dotenv()
app.config.update(dotenv_values())

db = SQLAlchemy(app)

app.register_blueprint(posts, url_prefix='/blog')
app.register_blueprint(handler, url_prefix='/telegram')


@app.context_processor
def set_context_vars():
    return dict(
        path=request.url
    )


@app.route('/')
def hello_world():  # put application's code here
    print('Key is: ', app.config['SECRET_KEY'])
    return render_template('index.html', title='Main page')


if __name__ == '__main__':
    app.run()
    executor.start_polling(dp)