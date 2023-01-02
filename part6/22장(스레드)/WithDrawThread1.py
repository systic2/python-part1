# WithDrawThread1 클래스(스레드 클래스)
# 멤버변수 : Account
# 생성자 : 조상클래스 생성자 호출
# 멤버메소드 : setAccount(Account) => 초기화 및 스레드명을 지정
# 멤버메소드 : run() => 출력결과를 보고 공유 객체 메소드를 호출
from Account import *


class WithDrawThread1(threading.Thread):
    def __init__(self):
        super().__init__()
        self.account = None

    def setAccount(self, account):
        self.account = account
        self.name = "어머니"

    def run(self):
        self.account.setBalance(1000)
        self.account.withDraw(500)
        self.account.withDraw(300)
