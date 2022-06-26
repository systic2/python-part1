# 사용자로부터 상품금액을 입력받아서 상품의 총 가격을 계산하는 프로그램 만들기
# 사용자가 몇 개의 상품을 살지 모르니깐 무한루프를 이용하고
# 아울러 사용자가 "끝"이라고 입력하면 루프를 탈출
from operator import eq

total = 0
number = 0
price = ''
print("종료하시려면 끝 이라고 입력해주세요.")
# 무한 루프 코드
while True:
    price = input("상품의 가격을 입력하세요 : ")
    # 끝 이라는 입력 문구가 있는지 확인하는 코드, 무한 루프를 탈출하는 코드
    if eq(price, '끝'):      # if price == "끝" 동일한 코드
        print("입력을 종료합니다.")
        if number == 0:
            print("입력하신 상품의 가격이 없습니다.")
            break
        else:
            print("입력하신 상품들의 갯수는 %d 개이고 총 가격은 %d 원입니다." % (number, total))
            break
    number += 1
    total += int(price)
