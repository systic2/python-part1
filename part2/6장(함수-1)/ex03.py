import calc

num1 = int(input("첫 번째 정수를 입력하세요 : "))
num2 = int(input("두 번째 정수를 입력하세요 : "))

print(f'입력하신 두 수는 {num1}, {num2} 이고 더 큰 수는 {calc.bigger(num1, num2)} 입니다.')

num1 = int(input("첫 번째 정수를 입력하세요 : "))
num2 = int(input("두 번째 정수를 입력하세요 : "))

print(f'입력하신 두 수는 {num1}, {num2} 이고 더 작은 수는 {calc.smaller(num1, num2)} 입니다.')

num1 = int(input("거듭제곱을 할 수를 입력하세요 : "))
num2 = int(input("거듭제곱 횟수를 입력하세요 : "))

print(f'{num1}를 {num2}번 거듭제곱한 수는 {calc.power(num1, num2)} 입니다.')