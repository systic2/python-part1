# 주사위 눈을 랜덤으로 발생시켜서 해당하는 숫자를 출력하는 프로그램
# randint() 함수를 검색하여 사용법을 익힌 후 프로그램을 작성

import random
# randint(a, b) 함수는 a부터 b까지 사이에 있는 정수를 반환해주는 함수
dice_num = random.randint(1, 6)
print(dice_num)

if dice_num == 1:
    print("주사위 눈은 1")
elif dice_num == 2:
    print("주사위 눈은 2")
elif dice_num == 3:
    print("주사위 눈은 3")
elif dice_num == 4:
    print("주사위 눈은 4")
elif dice_num == 5:
    print("주사위 눈은 5")
else:
    print("주사위 눈은 6")
# random() 함수는 0.0부터 1.0미만의 임의의 값을 float 형태로 반환해주는 함수
num = random.random()
print(num)
# randrange(start, stop, step) 함수는 start에서 stop까지 step의 값에 따라서
# 임의의 수를 반환해주는 함수
num = random.randrange(1, 101, 2)
print(num)
# randrange(a) 함수는 0에서부터 a 미만까지의 임의의 정수값을 반환해주는 함수
num = random.randrange(10)
print(num)