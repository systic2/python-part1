# 함수를 선언 및 구현
# 제곱을 구하는 함수
def jegop():
    number = int(input("정수를 입력하세요 : "))
    result = number * number
    return result

# 두 개의 정수를 입력받아서 두 수 중에서 더 큰 수를 찾아서 큰 수를 리턴하는 함수
def bigger(num1, num2):
    # return 문은 최소화하는게 좋은 코드이다
    temp = 0
    if num1 > num2:
        temp = num1
    else:
        temp = num2
    return temp

# 두 개의 정수를 입력받아서 두 수 중에서 더 큰 수를 찾아서 큰 수를 리턴하는 함수
def smaller(num1, num2):
    # return 문은 최소화하는게 좋은 코드이다
    temp = 0
    if num1 < num2:
        temp = num1
    else:
        temp = num2
    return temp

# 거듭제곱을 구하는 함수
def power(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result

