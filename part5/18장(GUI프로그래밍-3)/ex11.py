# 파일 열기, 저장 실습
# 파일 열기 filedialog 를 임포트 해야한다.
from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.title("파일 저장")
root.geometry("400x100")

lbl1 = Label(root, text="저장된 파일이름")
lbl1.pack()
# asksaveasfile() mode="w" 매개변수는 쓰기 모드라는 의미
# defaultextension=".jpg" 매개변수는 사용자가 확장자를 입력하지 않으면 기본적으로 jpg 확장자를 사용하겠다는 의미
# 파일포인터가 있어서 리소스를 사용하는 것이다.
saveFp = asksaveasfile(parent=root, mode="w", defaultextension=".jpg",
                       filetypes=(("jpg파일", "*.jpg"), ("모든파일", "*.*")))
lbl1.configure(text=saveFp)
# 리소스를 다 사용하면 반드시 close() 호출을 해야 한다.
saveFp.close()

root.mainloop()
