# 공유 객체를 사용하는 User1, User2 클래스의 인스턴스를 생성하여 실행시키는 코드 작성

from WithDrawThread1 import *
from WithDrawThread2 import *

if __name__ == '__main__':
    # 공유 객체 생성
    account = Account(0)
    # withdraw1 인스턴스를 생성하여 setter 를 호출하여 공유 객체의 주소를 넘기고 있다.
    withdraw1 = WithDrawThread1()
    withdraw1.setAccount(account)
    # withdraw2 인스턴스를 생성하여 setter 를 호출하여 공유 객체의 주소를 넘기고 있다.
    withdraw2 = WithDrawThread2()
    withdraw2.setAccount(account)
    # withdraw1, withdraw2 스레드 실행
    withdraw1.start()
    withdraw2.start()
