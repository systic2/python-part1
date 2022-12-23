# 대화상자의 생성과 사용에 대한 실습
from tkinter import *
from tkinter.simpledialog import *  # 사용자로 부터 입력을 받는 대화상자를 사용하기 위한 모듈 임포트

root = Tk()
root.geometry("400x100")

lbl1 = Label(root, text="입력된 값")  # 기본 텍스트 값을 지정함.
lbl1.pack()
# simpledialog 모듈에는 사용자로부터 숫자(askinteger), 문자열(askstring), 실수(askfloat)를 입력받을 수 있다.
value = askinteger("주사위", "주사위 숫자(1~6)를 입력하세요.", minvalue=1, maxvalue=6)

# 사용자로부터 입력받은 값을 lbl1 에 표시
lbl1.configure(text=str(value))

root.mainloop()
