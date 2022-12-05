# 추상클래스에 대한 실습
# 조상클래스 정의
from abc import *

class Unit(metaclass=ABCMeta):
    x = 0
    y = 0
    name = ""

    # 해당하는 Unit들은 움직임이 다 다르기 때문 추상메서드로 선언하였다.
    @abstractmethod
    def move(self, x, y):
        pass

    def stop(self, name, x, y):
        self.x = x
        self.y = y
        self.name = name
        print(f"현재 위치 : {self.x}, {self.y} 에 {self.name} 이/가 멈춥니다.")