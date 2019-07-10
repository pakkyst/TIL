from flask import Flask, render_template
import random
#flask에서 Flask만 꺼냄
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hi')
def hi():
    return 'Hi'


@app.route('/pick_lotto')
def pick_lotto():
    numbers = range(1, 46)
    lucky = random.sample(numbers, 6)
    return str(lucky)


# @app.route('/get_lotto/<int:num>')
# def get_lotto_1():
#     # 1회차 로또정보


@app.route('/pick_lunch/<count>')  # var routing
def pick_lunch(count):
    menus = {
        '짜장면',
        '짬뽕',
        '탕수육',
        '볶음밥'
    }
    picks = random.sample(menus, count)
    return str(picks)


@app.route('/cube/<int:num>')
def cube(num):
    return str(num ** 3)



if __name__ == '__main__':
    app.run(debug=True)