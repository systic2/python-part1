# 문제1
# 원(Circle)을 나타내는 클래스를 만들고 radius(반지름)을 생성자의 매개변수로 받아서 초기화하고
# getter(), setter(), area() 즉, 원의 면적을 구하는 메소드를 작성하고, Circle 클래스에
# +, >, < 연산자를 중복 정의 해보시오
# 출력결과
# c1의 반지름 : 4
# c2의 반지름 : 5
# c1의 반지름과 c2의 반지름을 합한 값 : 9
# c3 > c2의 결과 : True
# c1 < c2의 결과 : True
# 원의 반지름 : 9
# -------------------------------------------------------------------------
import math

class Circle:
    # 생성자
    def __init__(self, radius):
        self.radius = radius

    # getter() 메소드
    # def getter(self):
    #     return self.radius
    def getRadius(self):
        return self.radius

    # setter() 메소드
    # def setter(self, radius):
    #     self.radius = radius
    def setRadius(self, radius):
        self.radius = radius

    # 면적을 구하는 메소드
    def area(self):
        return math.pi * self.radius ** 2

    # 산술 연산자 중복 정의(+)
    def __add__(self, other):
        radius = self.radius + other.radius
        return Circle(radius)

    # 비교 연산자 중복 정의(>)
    def __gt__(self, other):
        return self.radius > other.radius

    # 비교 연산자 중복 정의(<)
    def __lt__(self, other):
        return self.radius < other.radius

    def __str__(self):
        return f"원의 반지름 : {self.radius}"


c1 = Circle(4)
c2 = Circle(5)
print(f"c1의 반지름 : {c1.getRadius()}")
print(f"c2의 반지름 : {c2.getRadius()}")
c3 = c1 + c2
print(f"c1의 반지름과 c2의 반지름을 합한 값 : {c3.getRadius()}")
print(f"c3 > c2의 결과 : {c3 > c2}")
print(f"c1 < c2의 결과 : {c1 < c2}")
print(c3)

