# 메모장 만들기
# 1단계 : GUI 만들기
# 2단계 : 파일 메뉴 기능 입히기
# 3단계 : 편집 메뉴 기능 입히기
# 4단계 : 도움말 메뉴 기능 입히기
from memo_main import *
from tkinter import *
from tkinter.filedialog import *
# 파일 이름을 가져오기 위해서 os 모듈을 임포트
import os

# 전역변수 초기화
es = ""


# 새 파일 클릭 시 호출되는 함수 정의
def new_file():
    top.title("제목없음-메모장")
    # 새 파일은 Text 위젯 안에 내용을 다 지우면 되는 것이다.
    # text 의 인덱스는 y.x 다시 말해서 x열을 사용한다.
    # 1.0은 첫 번째줄, 첫 번째 문자가 된다.
    ta.delete(1.0, END)


# 열기 메뉴 클릭 시 호출되는 함수 정의
def open_file():
    file = askopenfilename(title="파일 열기", filetypes=(("텍스트파일", ".txt"), ("모든파일", "*.*")))
    # 열려진 파일의 이름으로 타이틀 설정
    top.title(os.path.basename(file) + "-메모장")
    ta.delete(1.0, END)
    f = open(file, "r")
    # read() 는 파일 내용을 전부 문자열로 리턴해준다.
    # 문자셋을 서로 일치를 시켜줘야 한다. 메모장으로 ANSI로 저장하면 문제가 없다.
    ta.insert(1.0, f.read())
    f.close()


# 파일 저장 메뉴 클릭 시 호출되는 함수 정의
def save_file():
    f = asksaveasfile(mode="w", defaultextension=".txt")
    if f is None:  # 파일이 없으면 무효화 처리를 해주도록 한다.
        return
    # 저장하기 위해서 텍스트 위젯의 내용을 처음부터 끝까지 가져오는 코드
    ts = str(ta.get(1.0, END))
    f.write(ts)  # 파일 저장
    f.close()


# 종료 메뉴를 클릭 시 호출되는 함수 정의
def memo_exit():
    top.quit()
    top.destroy()


# 편집 메뉴 만들기
# 잘라내기 메뉴를 클릭 시 호출되는 함수 정의
def cut():
    global es
    # es 변수에게는 선택된 문자열을 저장한 후 삭제를 해야 한다.
    # 문자열의 인덱스는 시작이 SEL_FIRST, 마지막이 SEL_LAST로 접근이 가능하다.
    # 선택된 문자열 부분은 색상을 주도록 한다.
    es = ta.get(SEL_FIRST, SEL_LAST)
    ta.delete(SEL_FIRST, SEL_LAST)  # 잘라내기 한 부분은 지운다.


# 복사하기 메뉴를 클릭 시 호출되는 함수 정의
def copy():
    global es
    es = ta.get(SEL_FIRST, SEL_LAST)


# 붙이기 메뉴를 클릭 시 호출되는 함수 정의
def paste():
    global es
    # INSERT 상수는 커서의 위치를 가지고 있다.
    ta.insert(INSERT, es)


# 삭제 메뉴를 클릭 시 호출되는 함수 정의
def delete():
    ta.delete(SEL_FIRST, SEL_LAST)


# 도움말 메뉴를 클릭 시 호출되는 함수 정의
def help():
    he = Toplevel(top)
    he.geometry("200x200")
    he.title("정보")
    lbl = Label(he, text="메모장 버전 1.0\n파이썬으로 만든 메모장!")
    lbl.pack()


if __name__ == '__main__':
    top = Tk()
    top.title("메모장")
    top.geometry("400x400")

    ta = Text(top)  # 텍스트 위젯을 생성함
    sb = Scrollbar(ta)  # 텍스트 위젯의 스크롤바를 생성함
    sb.config(command=ta.yview())
    sb.pack(side=RIGHT, fill=Y)

    # 메모장의 기본 크기를 400, 400으로 설정했지만 필요하다면 크기를 확대시킬 수도 있다.
    # 이 때 Text 위젯이 자동으로 확대가 되기 위해서 아래와 같은 코드를 작성함.
    # weight 는 상대적인 크기를 나타내는 매개변수이며 1로 지정하면 전체화면의 크기에 맞춰 확장이 자동으로 이뤄진다.
    top.grid_rowconfigure(0, weight=1)  # 줄을 전체 크기로 설정함
    top.grid_columnconfigure(0, weight=1)  # 열을 전체 크기로 설정함
    ta.grid(sticky=N + E + S + W)  # Text 위젯이 좌우 상하를 다 채우도록 고정

    # 메뉴 만들기
    menuBar = Menu(top)
    fileMenu = Menu(menuBar, tearoff=False)  # 점선 없애기
    fileMenu.add_command(label="새 파일", command=new_file)
    fileMenu.add_command(label="열기", command=open_file)
    fileMenu.add_command(label="저장", command=save_file)
    fileMenu.add_separator()  # 분리선 추가
    fileMenu.add_command(label="종료", command=memo_exit)
    menuBar.add_cascade(label="파일", menu=fileMenu)  # 파일 메뉴를 메뉴바에 붙이기

    # 편집 메뉴 만들기
    editMenu = Menu(menuBar, tearoff=False)
    editMenu.add_command(label="잘라내기", command=cut)
    editMenu.add_command(label="복사", command=copy)
    editMenu.add_command(label="붙여넣기", command=paste)
    editMenu.add_command(label="삭제", command=delete)
    menuBar.add_cascade(label="편집", menu=editMenu)  # 편집 메뉴를 메뉴바에 붙이기

    # 도움말 메뉴 만들기
    helpMenu = Menu(menuBar, tearoff=False)
    helpMenu.add_command(label="메모장 정보", command=help)
    menuBar.add_cascade(label="도움말", menu=helpMenu)  # 도움말 메뉴를 메뉴바에 붙이기

    top.config(menu=menuBar)
    top.mainloop()
