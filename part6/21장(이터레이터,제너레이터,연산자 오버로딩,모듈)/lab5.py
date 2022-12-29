# 문제2
# 클래스 2개를 만드는데 먼저 Figure 클래스를 만들고 생성자에서 width와 height를 받아서 초기화한다.
# 그 다음 Quadrangle 클래스를 만들어 아래와 같이 출력결과가 나오도록 프로그램을 작성하시오
# 출력결과
# 너비의 합 : 5
# 높이의 합 : 7
# ------------------------------------------------------------------------------
# class Figure:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def __add__(self, other):
#         width = self.width + other.width
#         height = self.height + other.height
#         return Figure(width, height)
#
#
# class Quadrangle:
#     def __init__(self, figure):
#         self.figure = figure
#
#     def __add__(self, other):
#         return Quadrangle(self.figure + other.figure)
#
#
# fig1 = Figure(2, 3)
# fig2 = Figure(3, 4)
# qdr1 = Quadrangle(fig1)
# qdr2 = Quadrangle(fig2)
# qdr3 = qdr1 + qdr2
# print(f"너비의 합 : {qdr3.figure.width}")
# print(f"높이의 합 : {qdr3.figure.height}")

# 풀이
class Figure(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Quadrangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 연산자 + 중복 정의
    def __add__(self, other):
        return Quadrangle(self.width + other.width, self.height + other.height)


quad = Quadrangle(2, 3)
figure = Figure(3, 4)

print(f"너비의 합 : {(quad + figure).width}")
print(f"높이의 합 : {(quad + figure).height}")
print("------------------------------------")
