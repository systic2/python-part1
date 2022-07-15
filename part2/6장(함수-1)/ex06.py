# 간단한 사칙연산 계산기 만들기

# 더하기
def plus(x, y):
    return x + y

# 빼기
def minus(x, y):
    return x - y

# 곱하기
def multiple(x, y):
    return x * y

# 나누기
def divide(x, y):
    if y == 0:
        return "0으로는 나눌 수 없습니다."
    return round((x / y), 2)

temp = 'y'
# 계산기를 끄지 않으면 계속 되어야 한다.
while True:
    if temp == 'n':
        break
    elif temp == 'y':
        n1 = float(input("첫 번째 수 입력 :"))
        n2 = float(input("두 번째 수 입력 :"))
        op = input("원하는 연산을 입력(+, -, *, /) :")

        # 연산자에 의해 분기
        if op == "+":
            print(plus(n1, n2))
        elif op == "-":
            print(minus(n1, n2))
        elif op == "*":
            print(multiple(n1, n2))
        elif op == "/":
            print(divide(n1, n2))
        else:
            print('잘못된 연산자입니다.')
    temp = input("계산을 계속 하시겠습니까?(y or n) : ")

