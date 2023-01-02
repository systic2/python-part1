# 데몬스레드 실습
# 데몬(daemon) 스레드 : 종속성 스레드라고도 한다.
# 데몬스레드는 자신이 실행 중에 있어도 메인스레드가 종료를 하게 되면
# 따라서 같이 종료가 되는 것이 바로 데몬스레드이다.
# ex) 네이버 메일 작성 자동 저장, 파이썬 인터프리터와 같은 것이 바로 데몬스레드이다.
import threading
import time


class Worker(threading.Thread):
    # 생성자
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"작업스레드 시작 : {threading.current_thread().name}")
        time.sleep(3)
        # 메인스레드가 종료가 되니 이 부분은 아마 출력이 되지 않을 것이다.
        # 데몬스레드로 설정이 되어 메인스레드가 종료되니 데몬스레드는 메인스레드가 종료됨에 따라 같이 종료되기 때문이다.
        print(f"작업스레드 종료 : {threading.current_thread().name}")


if __name__ == '__main__':
    print("메인스레드 시작")
    for i in range(5):
        name = str(i)
        thread = Worker(name)
        # print(f"thread가 데몬입니까? {thread.daemon}")
        # daemon 변수에 저장되어 있는 스레드 인스턴스를 데몬스레드로 바꾼다.
        # daemon 속성 기본값은 False 이지만, 데몬스레드로 만들기 위해서는 이 속성의 값을 True로 설정해야 한다.
        thread.daemon = True
        # print(f"thread가 데몬입니까? {thread.daemon}")
        thread.start()
    print("메인스레드 종료")
