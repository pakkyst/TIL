from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return 'hi'


@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    end_date = datetime.datetime(2019, 11, 29)
    left = end_date - today
    return render_template('dday.html', left_days=left.days)
    # f'SSAFY 2기 1학기 종료일까지 {left.days} 일 남았습니다.'


@app.route('/boxoffice')
def boxoffice():
    top_5 = [
        '스파이더맨 파 프롬 홈',
        '알라딘',
        '토이스토리4',
        '존윅3',
        '라이온킹'
    ]
    return render_template('boxoffice.html', movies=top_5) #a=b구조를 보기 위해 이름 다르게


if __name__ == '__main__':
    app.run(debug=True)
