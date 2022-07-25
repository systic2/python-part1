# 원의 면적과 원의 둘레를 구하는 프로그램을 작성하는데
# PI = 3.141592 전역 상수를 선언하고 상수를 활용하도록 한다.

PI = 3.141592

# 프로그램 시작 함수
def main():
    r = float(input("원의 반지름을 입력하세요 : "))
    c1 = circle_length(r)
    c2 = circle_area(r)
    print(c1, c2)

# 원의 면적을 구하는 함수를 선언 및 구현
# 원의 면적 공식 : PI * 반지름의 제곱
def circle_area(r):
    return PI * r ** 2

# 원의 둘레를 구하는 함수를 선언 및 구현
# 원의 둘레 공식 : 2 * PI * 반지름
def circle_length(r):
    return 2 * PI * r

# 프로그램 시작을 알림
main()

