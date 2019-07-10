## 함수 QUIZ

**#input() : 입력을 시작한다**

```python
name = input(질문 'What is your name?')
# = What\'s your name?
#오른쪽부터 읽는게 원칙
#What is your name?에 대한 답을 기다리고, 그에 대한 입력값을 name에 넣는다.
print('hi,  ' + name)
```

- 사람이 어떤 액션을 취하지 않는 이상 코드가 끝나지 않음

- 끝나지 않기 때문에 바로 다른 명령 불가, 다른 명령을 하려면 터미널에서 +에서 추가
- ctrl + C : Cancel
- ctrl + D : exit(터미널종료)



- $(in 터미널) : 프롬프터 - "말해도돼" - 명령어를 들을 준비가 되어있다

​	ex. ls, mkdir



```python
#Words 의 첫 글자와 마지막 글자를 출력하라
words = input('입력 고고: ')
print(words[0], words[-1])

#리스트뿐만 아니라

words = input('입력 고고: ')
print(type(words)) #<class 'str'> str : 문자열
print(words[0], words[-1])
#words의 type이 무엇인가

#리스트화시켜서 리스트의 처음과 마지막 글자 출력
my_list = list(words)
print(my_list[0], my_list[-1])


import random
length = random.choice(range(1, 100))
numbers = list(range(length))
#length - 1 ex. length = 50 [1, 2, ... 49]
numbers[-1] : 마지막숫자
print(numbers[length-1])
print(numbers[-1])
```



```python
# 자연수 n 을 입력받고, 1부터 n까지 출력하라
n = input('자연수를 입력하세요')
n = int(n)
my_list = list(range(1, n+1))
print(my_list)

#str은 리스트가 될 수 있다.
#str => list(str)
#str => int(str) : 따옴표를 없앴을 때 정수인 애들은 가능 ex. '10'=>10

#for문
n = list(range(1, numbers + 1))
for numbers in n:
    print(numbers)
    numbers + 1
    
#뭐를 입력해도 1~10
n = input('자연수를 입력하세요')
n = 10
for i in range(n):
    print(i + 1)
    
n = input('자연수를 입력하세요')
n = int(n)
for i in range(n):
    print(i + 1)

n = input('자연수를 입력하세요')
n = int(n)
for i in range(n):
    print(i + 1, end=' ')
```





#### 코드 쪼개기  & 합치기 : 가독성

```python
#짝수/홀수를 구분하자
string = input('숫자를 입력하세요: ')
numbers = int(string)

numbers = int(input('숫자를 입력하세요: '))

if numbers %2 == 0:
    print('짝수')
else:
    print('홀수')
```

- %는 몫이 아닌 나누고 남은 나머지 

  ex. 100 % 6 = 4

```python
#3배수 fizz, 5배수 buzz, 15배수 fizzbuzz
numbers = input('자연수를 입력하세요')
numbers = int(numbers)

for i in range(1, numbers + 1):
    if i % 15 == 0:
        print('fizz buzz')
    elif i % 5 == 0:
        print('buzz')
    elif i % 3 == 0:
        print('fizz')
    else:
        print(i)
```



**데이터를 가져오는 방법**

1. web scrapping : 사람이 직접 웹 정보를 긁어오는 것 = 귀찮음

2. web API : 프로그래머가 보기 위한것(dict)

3. package, module : 서비스 제공자가 제공(코드가 가장 짧음)



? & 기준으로 끊어서 읽기

​	ex. https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866

​	 https://www.dhlottery.co.kr/common.do

​	?method=getLottoNumber

​	&drwNo=866



API를 통해 사용자가 받아오는 정보는 str



## Get Lotto

```python
import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'

response = requests.get(url).text
print(response['bnusNo'])

error

print(type(response)) - str으로 나옴, dic이 아니었음



import requests
import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'

response = requests.get(url).text

data = json.loads(response)
# print(type(data), data)
print(data['bnusNo'])

real_numbers = []
# for i in range(6):
#     real_numbers[i] = data[f'drwtNo{i+1}']

for key, value in data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)

print(real_numbers)

#Dic에서는 key값만 뽑을 수 있는데, items()를 통해 value값까지 같이 뽑기 가능.
#for key, value in data.items():
```



```python
import random
random.choice([1,2,3,4,5])
#필통을 꺼내고 연필을 꺼낸다


from random import choice
choice([1,2,3,4,5])
#필통에서 연필만 꺼낸다
```





## html


    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
        </head>
        <body>
            <h1>Today I Learned</h1>>
            <h2>Learn Flask</h2>
            <ol>
                <li>pip install flask</li>
                <li>touch app.py</li>
                <li>python app.py</li>
            </ol>
            <h2>Learn HTML</h2>
            <ul>
                <li>doctype</li>
                <li>head, body</li>
            </ul>
        </body>
    </html>
</html>
</!doctype>

head 에 넣은 내용은  안보임

body 에 넣은 내용은 보임