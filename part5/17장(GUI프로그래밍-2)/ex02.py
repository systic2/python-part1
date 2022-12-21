# 레이블에 이미지와 텍스트를 동시에 나타내기

from tkinter import *

window = Tk()
# PhotoImage 클래스는 jpg 확장자를 지원을 하지 않는다.
photo = PhotoImage(file="images/christmas.png")
# 이미지가 들어가 있는 레이블은 윈도우의 우측에 배치
lbl1 = Label(window, image=photo)
# lbl1.photo = photo
lbl1.pack(side=RIGHT)
msg = """
안녕하세요. 메리 크리스마스 산타할아버지는 모든 것을 알고 계신데
안녕하세요. 메리 크리스마스 산타할아버지는 모든 것을 알고 계신데
안녕하세요. 메리 크리스마스 산타할아버지는 모든 것을 알고 계신데
안녕하세요. 메리 크리스마스 산타할아버지는 모든 것을 알고 계신데
"""

# 텍스트를 출력
Label(window,
      justify=LEFT,  # 텍스트를 왼쪽정렬
      padx=10,
      text=msg
      ).pack(side=LEFT)

window.mainloop()
