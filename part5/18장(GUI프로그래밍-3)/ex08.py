# 기능이 추가하는 메뉴를 생성하는 실습
from tkinter import *
from tkinter import messagebox

# 함수 정의
def func_open():
    messagebox.showinfo("메뉴선택", "열기 메뉴를 선택함")

def func_exit():
    root.quit()
    root.destroy()  # 윈도우를 메모리에서 제거

# 메인 코드 부분
root = Tk()

mainMenu = Menu(root)   # mainMenu 변수에 Menu 생성. 소유자가 root가 된다.
root.config(menu=mainMenu)  # 윈도우에 메뉴는 mainMenu 라고 지정하는 것이다.

fileMenu = Menu(mainMenu, tearoff=False)
# 다른 메뉴가 확장이 되어야 되기 때문에 add_cascade() 사용하여 메뉴의 이름을 "파일"로 설정하였고
# menu 속성값을 fileMenu로 지정
mainMenu.add_cascade(label="파일", menu=fileMenu)

# 하위 메뉴 만들기
fileMenu.add_command(label="열기", command=func_open)     # 열기 버튼을 클릭하면 func_open 함수 호출
fileMenu.add_separator()    # 구분선
fileMenu.add_command(label="종료", command=func_exit)     # 종료 버튼을 클릭하면 func_exit 함수 호출

root.mainloop()
