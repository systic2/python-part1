# 숫자 추측 게임을 만들기

from random import *
# 1~100까지 임의의 수를 발생시키는 코드
rand_num = randint(1, 100)
print(rand_num)
cnt = 0
while True:
    user_num = int(input("숫자를 맞춰보세요.(1 ~ 100) : "))
    cnt += 1 # 파이썬에서는 ++, -- 이런 증감 연산자는 없다. 복합대입연산자를 사용

    if user_num == rand_num:
        print(f"정답입니다. 게임을 종료합니다.(시도횟수 : {cnt})")
        break
    elif user_num > rand_num:
        print("입력한 숫자가 큽니다.")
    else:
        print("입력한 숫자가 작습니다.")
