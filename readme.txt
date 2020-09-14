1. 필용한 라이브러리
	1) Tkinter : 기본 내장된 라이브러리
	2) wxPython
	3) PyQt
	...

2. 라이브러리 준비
    1) http://wxpython.org/Phoenix/snapshot-builds
            >	wxPython-4.1.1a1.dev4952+e5021fb5-cp37-cp37m-win_amd64.whl	2020-09-11 03:23	17M
            - 다운로드 받은 파일의 확장자를 zip으로 수정하고 압축을 풀어준다.
                wx폴더를 파이썬 설치폴더/lib/site-package 에 복사
            - 다운로드 받은 파일(.whl) 위치에서 콘솔창을 열고 아래와 같이 명령을 실행
                pip install 파일명
    2) 개발툴이 pycharm일 경우
            - File > Settings > Project:프로젝트명 > Progject Interpreter
                + 버튼을 누르고 설치하고자 하는 라이브러리 검색 후 install package 버튼 클릭