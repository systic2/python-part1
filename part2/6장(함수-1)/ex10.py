# 구의 부피를 계산하는 함수 sphereVolume()를 작성하여 보자
# 그리고, 반지름을 사용자로부터 입력을 받고 구의 부피를 구하는 함수를 호출해서 테스트
# 구의 부피 공식 : 4/3 * pi * r의 세제곱
import math

# 구의 부피를 구하는 함수를 선언 및 구현
def sphereVolume(radius):
    PI = math.pi
    volume = (4/3) * PI * (radius**3)
    return round(volume, 2)

radius = float(input("반지름을 입력해주세요 : "))
print(f'반지름 : {radius}인 구의 부피 : {sphereVolume(radius)}')
