import json
import os
from random import randint
from datetime import datetime

from flask import Flask, render_template
from werkzeug.exceptions import NotFound
import json

app = Flask(__name__)


def get_current_date():
    current_date = datetime.now().date()
    return current_date


@app.route('/')
def main():
    current_date = get_current_date()
    r, g, b = randint(0, 256), randint(0, 256), randint(0, 256)
    return render_template('index.html', date=current_date, r=r, g=g, b=b)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
