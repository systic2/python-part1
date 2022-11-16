# 문제
# 원(Circle)을 클래스로 표시해보자. 원은 반지름(radius)을 가지고 있다.
# 원의 넓이와 둘레를 계산하는 메소드를 정의해보자.
# 생성자는 매개변수가 존재하는 생성자를 만들어보자.
# 출력결과
# 원의 반지름 : 10
# 원의 넓이 : 314.1592
# 원의 둘레 : 62.83
import math


# 클래스 정의
class Circle:
    __radius = 0

    def __init__(self, radius):
        self.__radius = radius

    # getter(), setter() 메서드 제공
    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    # 원의 넓이를 구하는 메서드
    def calcArea(self):
        return round(math.pi * self.__radius ** 2, 2)

    # 원의 둘레를 구하는 메서드
    def calcCircumference(self):
        return round(2 * self.__radius * math.pi, 2)

    # 출력하는 메서드
    def __str__(self):
        print("원의 반지름 : ", self.__radius)
        print("원의 넓이 : ", Circle.calcArea(self))
        print("원의 넓이 : ", Circle.calcCircumference(self))


if __name__ == "__main__":
    circle1 = Circle(10)
    circle1.__str__()
