# GUI 프로그램에서 람다식을 활용한 예제
# 이벤트 처리 시 람다식으로 콜백함수를 지정
from tkinter import *

window = Tk()
btn1 = Button(window, text="버튼1", command=lambda : print("버튼1이 눌러짐"))
btn1.pack(side=LEFT)
btn2 = Button(window, text="버튼2", command=lambda : print("버튼2이 눌러짐"))
btn2.pack(side=LEFT)
quitBtn = Button(window, text="종료", fg="red", command=quit)
quitBtn.pack(side=LEFT)
window.mainloop()
