# HTML

- 이미지
  - 링크 : 수정, 편리
  - 저장 : 로드 속도가 빠름, 원작 이미지가 지워져도 문제X

- CSS



- 같은 Class를 가진 애들은 수정 사항 동시 적용





```html
# ! + tab

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    
</body>
</html>

```



```python
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


if __name__ == '__main__':
    app.run(debug=True)
    
#app.route : 길을 터준다
```

```html
#dday.html

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>D-day</title>
</head>
<body>
    <h1>SSAFY 1학기 종료까지</h1>
    <h2>{{ left_days }}일 남았습니다.</h2>
</body>
</html>
```

{{}} = print

%% logical

```python
@app.route('/boxoffice')
def boxoffice():
    top_5 = [
        '스파이더맨 파 프롬 홈',
        '알라딘',
        '토이스토리4',
        '존윅3',
        '라이온킹'
    ]
    return render_template('boxoffice.html', movies=top_5) #a=b구조를 보기 위해 이름 다르게 시도
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

    <title>Box Office</title>
</head>
<body>
    <h1>box office</h1>
    <ol>
        {% for movie in movies %}
            <li>{{ movie }}</li>
        {% endfor %} 
    </ol>
</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Send message</title>
</head>
<body>
    <h1>Send message here</h1>
    <form>
        <input type="text" placeholder="message here" autofocus>
        <input type="submit">
    </form>
</body>
</html>

#autofocus : 껌뻑껌뻑
#palceholder : 미리써놓기(지우지 않아도 됨)

        <input type="text" value="hi">
        <input type="submit" value="보내기">

#value : 미리써놓기(지우고 써야함)
#Submit - 제출(디폴트) - 보내기로 변경
```







```python
@app.route('/send')
def send():
    return render_template('send.html')


@app.route('/receive')
def receive():
    data = request.args.get('msg')
    return render_template('receive.html', data=data)
```

#send.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Send message</title>
</head>
<body>
    <h1>Send message here</h1>
    <form action="/receive">
        <input type="text" name="msg">
        <input type="submit" value="보내기">
    </form>
</body>
</html>
```

#receive.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>수신함</title>
</head>
<body>
    <h1>{{ data }}</h1>
</body>
</html>
```



#Name과 Id의 차이

name : 서버에서 문서를 받아보라고

id : 문서 내에서 한 개만 존재 가능 - 특정 무언가를 잡아낼 때 사용





#회사명 검색으로 주식정보 출력

```python
from iexfinance.stocks import Stock

@app.route('/receive')
def receive():
    data = request.args.get('msg')
    stock = Stock(data, token='pk_63c229409ff14b67a6cc81e38927f1c4').get_quote()
    return render_template('receive.html', stock=stock)
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>수신함</title>
</head>
<body>
    <h1>{{ stock }}</h1>
</body>
</html>
```



**#X + Y더하기**

```python
@app.route('/add')
def add():
    return render_template('add.html')
    
@app.route('/result')
def result():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    result = num1 + num2

    return render_template('result.html', result=result)
```

#add.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ADD 2 numbers</title>
</head>
<body>
    <h1>Plus</h1>
     <form action="/result">
        <input type="number" placeholder="숫자" name="num1" autofocus>
        <input type="number" placeholder="숫자" name="num2">
         <input type="submit" value="더하기">
      </form>
</body>
</html>
```

type : number - 숫자만 쓸 수 있음.



#result.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>result</title>
</head>
<body>
    <h1>{{ result }}</h1>
</body>
</html>
```

