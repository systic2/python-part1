from math import *
# 파이썬에서의 자료형(Data-type)
# int형을 출력
print(type(17))

# float형을 출력
print(type(10.7777789))

# str형을 출력
print(type("안녕하세요"))

# 반지름이 r인 구의 부피는 4/3 * PI * r의 세제곱
# 반지름이 5인 구의 부피를 계산하는 프로그램
r = 5.0
# volume = 4.0/3.0 * pi * r ** 3
volume = 4.0/3.0 * pi * pow(r, 3)
print("구의 부피 : " + str(volume))

# 구의 겉넓이 공식 : 4 * pi * r의 제곱
outer_area = 4 * pi * pow(r, 2)
print("구의 겉넓이 :", outer_area)