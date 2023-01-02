import winsound
import time
import threading

# 윈도우의 비프음 발생시키는 코드
# fr = 2000   # 주파수(범위 : 37~32767)
# du = 1000   # 1000ms => 1초
# for i in range(3):
#     winsound.Beep(fr, du)
#     time.sleep(1)   # second 단위 1초간 일시정지

# 싱글스레드 환경
# 아래 코드는 싱글 스레드에서 돌아가는 작업이다.
# 그래서 비프음을 3번 알리고 난 후, "삐~~"라는 문자열이 3번 출력된다.
# 우리가 원하는 것은 콘소렝 "삐~~~" 문자열과 함께 비프음도 같이 나길 원하는 것이다.
# 이렇게 하고자 한다면 스레드를 하나 만들어 멀티 스레드로 바꿔야 한다.
# print(f"현재 실행중인 스레드명 : {threading.current_thread().name}")
# fr = 2000  # 주파수(범위 : 37~32767)
# du = 1000  # 1000ms => 1초
# for i in range(3):
#     print(f"현재 실행중인 스레드명(1번째 for 문) : {threading.current_thread().name}")
#     winsound.Beep(fr, du)
#     time.sleep(1)  # second 단위 1초간 일시정지
# for i in range(3):
#     print(f"현재 실행중인 스레드명(2번째 for 문) : {threading.current_thread().name}")
#     print("삐~~~~~~")
#     time.sleep(1)


# 문제1
# 위와 같은 싱글스레드에서 실행하는 것을 멀티 스레드로 코드를 바꾸어서
# "삐~~" 문자열과 비프음이 동시에 실행되는 코드를 작성하시오.
# ----------------------------------------------------
fr = 2000  # 주파수(범위 : 37~32767)
du = 1000  # 1000ms => 1초


class BeepSound(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"현재 실행중인 스레드 : {threading.current_thread().name}")
        for i in range(3):
            winsound.Beep(fr, du)
            time.sleep(1)  # second 단위 1초간 일시정지


# class BeepPrint(threading.Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         print(f"현재 실행중인 스레드명(2번째 for 문) : {threading.current_thread().name}")
#         for i in range(3):
#             print("삐~~~~~~")
#             time.sleep(1)


if __name__ == '__main__':
    print(f"현재 실행중인 스레드 : {threading.current_thread().name}")
    beepsound = BeepSound("BeepSound")
    # beepprint = BeepPrint("BeepPrint")
    beepsound.start()   # run() 자동 호출됨
    # beepprint.start()
    # beepsound.join()
    # beepprint.join()
    # "삐~~" 문자열을 출력시키는 코드
    for i in range(3):
        print("삐~~~~~")
        time.sleep(2)
    # 위와 같이 두 개의 스레드로 병렬성과 동시성을 이용하여
    # "삐~~"라는 문자열 출력과 비프음을 동시에 출력할 수 있음을 알 수 있다.

    # 스레드는 재사용이 안된다.
    # 오직 한 번만 실행한다.
    # 재사용하고자 한다면 다시 스레드 인스턴스를 생성하여 start() 호출해야 한다.(중요)
    thread1 = BeepSound("BeepSound-1")
    thread1.start()
