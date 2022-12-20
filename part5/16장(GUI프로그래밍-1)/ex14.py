# 온도 변환기 UI 만들기
from tkinter import *
# 이벤트 처리함수를 정의
def process():
    # e1 엔트리 클래스에서 사용자가 입력한 값을 get()를 통해서 가져옴
    tf = float(e1.get())
    tc = (tf-32.0)*5.0/9.0  # 화씨에서 섭씨로 변경함
    e2.delete(0, END)   # e2 엔트리의 값을 처음부터 끝까지 다 지운다.
    e2.insert(0, str(tc))

window = Tk()

Label(window, text="화씨").grid(row=0, column=0)
Label(window, text="섭씨").grid(row=1, column=0)
# 아래와 같이 분리를 해줘야 NoneType 에러를 발생시키지 않는다.
e1 = Entry(window)
e1.grid(row=0, column=1)
e2 = Entry(window)
e2.grid(row=1, column=1)

Button(window, text="화씨=>섭씨", command=process).grid(row=2, column=1)

window.mainloop()
