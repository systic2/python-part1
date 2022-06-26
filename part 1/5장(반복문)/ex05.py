# for 문을 이용하여 팩토리얼(factorial)을 계산하는 프로그램을 작성
# 팩토리얼 n! 은 1부터 n까지의 정수의 모두 곱한 것을 의미

factorial = 1

num = int(input("정수를 입력하세요 : "))

for i in range(1, num+1):
    factorial = factorial * i # factorial *= i

print(f"{num}! = {factorial}")