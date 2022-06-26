# 1부터 사용자가 입력한 수 num까지 더해서 합계를 구하는 프로그램을 for문을 이용해 작성

user_num = int(input("숫자를 입력하세요 : "))

hap = 0
for i in range(1, user_num + 1):
    hap += i        # 복합대입연산자(값을 누적하거나 차감할 때 사용하는 연산자)
print("1부터 입력한 숫자까지의 합 : ", hap)
