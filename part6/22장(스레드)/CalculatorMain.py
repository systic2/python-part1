# 공유 객체를 사용하는 User1, User2 클래스의 인스턴스를 생성하여 실행시키는 코드 작성

from User1 import *
from User2 import *

if __name__ == '__main__':
    # 공유 객체 생성, memory 값을 0으로 초기화
    calculator = Calculator(0)
    # User1 인스턴스를 생성하여 setter 를 호출하여 공유 객체의 주소를 넘기고 있다.
    user1 = User1()
    user1.setCalculator(calculator)
    # User2 인스턴스를 생성하여 setter 를 호출하여 공유 객체의 주소를 넘기고 있다.
    user2 = User2()
    user2.setCalculator(calculator)
    # User1, User2 스레드 start() 시킨다
    user1.start()
    user2.start()
