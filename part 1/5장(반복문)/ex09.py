# 사용자로부터 2개의 정수 값을 입력받고 첫 번째 입력받은 값부터
# 두 번재 입력받은 값까지의 범위에서 3의 배수이고 4의 배수를 제외하고 출력하는 프로그램

num1 = int(input("첫 번재 정수 입력 : "))
num2 = int(input("두 번째 정수 입력 : "))

# print("3의 배수이면서 4의 배수는 아닌 수들")
# for i in range(num1, num2+1):
#     if (i % 3 == 0) and (i % 4 != 0):
#         print(i, end=" ")

print("3의 배수이면서 4의 배수는 아닌 수들")
for i in range(num1, num2+1):
    if (i % 3 == 0) and (i % 4 == 0):
        continue        # continue는 조건식이 참이면 아래 문장을 실행하지 않고 for 문으로 이동하여 증가
    print(i)