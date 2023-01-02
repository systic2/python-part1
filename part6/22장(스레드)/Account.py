# 문제3
# 파이썬 파일 4개가 나와야 한다.
# Account 클래스(공유 객체)
# 멤버변수 : balance
# 생성자 : 조상클래스 생성자 호출
# 멤버메소드 : getBalance() => 1초 일시정지 후 balance 리턴
# 멤버메소드 : setBalance(Balance) => 2초 일시정지 후 balance 값을 변경(동기화 처리 필요)
# 멤버메소드 : withDraw() => 1초 일시정지 후 잔액 결과 출력 및 예외 처리(동기화 처리 필요)
# ----------------------------------------------------------
# WithDrawThread1 클래스(스레드 클래스)
# 멤버변수 : Account
# 생성자 : 조상클래스 생성자 호출
# 멤버메소드 : setAccount(Account) => 초기화 및 스레드명을 지정
# 멤버메소드 : run() => 출력결과를 보고 공유 객체 메소드를 호출
# ----------------------------------------------------------
# WithDrawThread2 클래스(스레드 클래스)
# 멤버변수 : Account
# 생성자 : 조상클래스 생성자 호출
# 멤버메소드 : setAccount(Account) => 초기화 및 스레드명을 지정
# 멤버메소드 : run() => 출력결과를 보고 공유 객체 메소드를 호출
# ----------------------------------------------------------
# AccountMain 클래스(실행 파일)
# 공유 객체 생성 및 스레드 생성 그리고 start()
# ------------------------------------------------------------
# 출력결과(달라질 수 있다.)
# 어머니 이/가 입금 : 1000원
# 어머니 이/가 출금 : 500원
# 통장 잔액 : 500원
# 아들 이/ 출금 : 300원
# 통장 잔액 : 200원
# 어머니 이/가 300원 출금 시도하였습니다.
# 잔액이 부족합니다!
import threading
import time

lock = threading.Lock()


class Account:
    def __init__(self, balance):
        super().__init__()
        self.balance = balance  # 계좌금액 초기화

    def getBalance(self):
        time.sleep(1)
        return self.balance

    def setBalance(self, balance):
        lock.acquire()  # 잠금 시작
        self.balance += balance     # 입금액으로 잔액을 바꿈
        time.sleep(2)   # 2초간 일시정지
        # 현재 실행중인 스레드 이름과 balance 값을 출력하는 코드
        print(f"{threading.current_thread().name} 이/가 입금 : {balance}원")
        print(f"통장 잔액 : {self.balance}원")
        lock.release()  # 잠금 해제

    def withDraw(self, money):
        lock.acquire()
        if money > self.balance:    # 잔액이 출금 금액보다 작으면
            try:
                time.sleep(1)
                print(f"{threading.current_thread().name} 이/가 {money}원 출금 시도하였습니다.")
                raise Exception()
            except Exception:
                print("잔액이 부족합니다!")
        else:   # 잔액이 출금 금액보다 더 많으면
            time.sleep(1)
            self.balance -= money
            print(f"{threading.current_thread().name} 이/가 출금 : {money}원")
            print(f"통장 잔액 : {self.balance}원")
        lock.release()
