import os
from os.path import join, dirname

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, dotenv_values

from posts.blueprint import posts


app = Flask(__name__)
load_dotenv()
app.config.update(dotenv_values())

db = SQLAlchemy(app)

app.register_blueprint(posts, url_prefix='/blog')


@app.route('/')
def hello_world():  # put application's code here
    print('Key is: ', app.config['SECRET_KEY'])
    return render_template('index.html', title='Main page')


if __name__ == '__main__':
    app.run()