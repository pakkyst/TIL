# what is git

git: scm (source code manager) / vcs (version control system)

버전 관리를 해주는 cctv



`git init`: 이 dic에 git을 넣음 - master가 붙음

`cd dic명`: dic으로 들어가기

`cd ..`: 위의 dic으로 가기

`touch file명`: fiie 생성

`mkdir dic명`: dic 생성

`rm dic명`: dic 삭제

`git status`: dic 안의 상태 명시

`ls`: list. 내 상태에서 무엇이 있는가 리스트로 보여줘.

`git add <filename>`: git 이 file 감시해줘

`git commit -m 'message'` : 이 메세지로 저장해줘

`git add <filename>`: git이 사진 찍을 수 있도록 멈춰 (변경사항 저장 후 다시 재저장하기 전)

`git log`:  사진(commit/ 저장사항)들의 로그를 보여줌 (최신부터 역순으로 보여줌)

`git push`: git에 백업하기

`git remote add <drive name>`:  내 백업은 여기로 보내

`git remote -v`: 내 백업 공간은 어디야?

`git push <drive name> master`:  origin으로 백업 해줘

`git add -A`: 여러개를 한 번에 저장할게

`git add . ` : 여러 개를 한 번에 저장할게

#tab 누르면 파일명을 쉽게 쓸 수 있음

#'touch.gitignore' : gitignore이라는 git에서 숨겨진 dic을 생성



## 내 git sign

````git
git config-global user.email "email"

git config-global user.name "name"
````







## WEB 브라우저 열기

```python
import webbrowser

urls = [
    'www.google.com',
    'www.naver.com',
    'www.github.com'
]

for url in urls:
     webbrowser.open(url)


i = 0
while i < 3:
    webbrowser.open(urls[i])
    i = i + 1
```





## Web에서의 커뮤니케이션 방식

요청 ---------주소(URL)-------------> 응답

​          <---문서(HTML, XML 등)---



주소로 요청을 보내고, 응답을 문서로 받음



pip = 내부에 없는 것을 외부에서 사오기?

`pip install <함수명>` : 내 책상 위에도, 서랍 안에도 없는 함수를 다운로드

ex. pip install requests



```python
import requests

response = requests.get('https://naver.com').text
print(response)

```



#'.text'가 없으면 줄 수만 출력 ex. 200

있으면 페이지 전체 출력



```python
import requests
import bs4 

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
text = bs4.BeautifulSoup(response, 'html.parser')
kospi = text.select_one('#KOSPI_now')

print(kospi.text)
```

bs4 : 사람이 보기엔 똑같지만, python이 보기 쉽게 만들어주는 역할

text = bs4.BeautifulSoup(변수) : 출력될 변수인 페이지 소스를 bs에 한 번 넣어주는 것



* ctrl + c   > 잘못 눌렀을 경우 지금까지 과정 취소
* ctrl / : 전체 #





멜론 top50

```python
import bs4
import requests

url = 'https://www.melon.com/chart/index.htm'

headers = {'User-Agent': ':)'}

response = requests.get(url, headers=headers).text
text = bs4.BeautifulSoup(response, 'html.parser')
rows =text.select('.lst50')

for row in rows:
    rank = row.select_one('td:nth-child(2) > div > span.rank').text
    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
#여러개의 값 출력 가능
    print(rank, title, artist)
```



headers = {'User-Agent': ':)'} 

* 모든 홈페이지에서 요청한다고 주는 것은 아니고, 요청이 약간의 변형이 필요한 경우가 있다.

## File control



```python
lunches = {
    #Key값       #Value값
    #Key와 Value값을 같이 페어로 꺼내는게 포인트
    '양자강' : '02-557-4565',
    '김밥카페' : '02-586-4501',
    '순남시래기' : '02-456-5486'
}

with open('lunch.csv', 'w', encoding='utf-8') as f:
    for lunce in lunches:
    print(lunch)
```



```python
import csv

with open('lunch.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f)
    for item in items:
        print(item)
```

CSV (comma seperate value)





file_write

```python
lunches = {
    '양자강' : '02-557-4565',
    '김밥카페' : '02-586-4501',
    '순남시래기' : '02-456-5486'
}

with open('lunch.csv', 'w', encoding='utf-8') as f:
    f.write('식당이름, 전화번호\n')
    for name, phone in lunches.items():
        f.write(f'{name}, {phone}\n')

# print(lunch)
# print(lunches[lunch])

# for k, v in lunches.items():
#     print(name, phone)
```



​	