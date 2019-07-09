# What is Git?

1. git : scm / vcm

   scm : source code manager

   vcs : version control system



​	ex. 최종.pptx 최종_수정.pptx 최종최종2.pptx



- 뒤로 돌아갈 수도 있다는 사실에 이전 버전 저장

  최종발표v1.pptx, 최종발표v2.pptx, 최종발표v3.pptx ...  당시 어떤 이슈가 있는지 알 수X

  -- 최종발표v1_1차완료본,  최종발표v2_챕터2삭제



git = 버전관리를 해주는 감시카메라? : git은 변화를 감지



우클릭 git bash - git init = git이 이제 관리를 한다

- cd : 폴더 이동
- cd til : TIL의 master 삭제
- mkdir X : X 폴더 생성
- touch final.txt : final 문서 파일 생성 / touch = 생성
- ls : List 내 상태에 어떤 것이 있는가
- rm X : X삭제
- git add <file name> : 파일을 내내 예의주시하며 감시
- git status : 지금 상태?
- git add : 새로운 상태를 사진찍을?상태가 되었다
- git log : 찍은 사진들의 리스트



git commit -m '처음 만들었음'

git config --global user.email 'pakkyst@gmail.com'

git config --global user.name 'Joon Young Pak'



`git init`

`git add <file name>`

`git commit -m '<message>'`

변경사항 저장

`git add <file name>`

`git commit -m '<message>'`

...



`git status` : 상태를 물어보는 명령어

`git log` : 사진(Commit)들 로그를 보여줌



