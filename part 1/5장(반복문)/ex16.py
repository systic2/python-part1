# 플래그 변수를 사용한 무한 루프 문제
# 1. 증속, 2. 감속, 3. 중지 를 출력하고 사용자의 입력을 1, 2, 3 받아서
# 증속을 하면 속도를 10씩 증가하고 출력
# 감속을 하면 속도를 10씩 감소하고 출력
# 중지를 하면 플래그 변수를 이용하여 무한 루프를 빠져나간다

run = True

speed = 0

while run:
    user_input = int(input("1. 증속, 2. 감속, 3. 중지 : "))
    # 중지일 경우 플래그 변수를 False로 설정해줌으로써 무한 루프를 탈출하는 코드
    if user_input == 3:
        run = False
        print("프로그램을 종료합니다.")
        print(f"속도는 {speed}km입니다.")
    # 증속일 경우
    elif user_input == 1:
        speed += 10
        print(f"현재 속도는 {speed}km!")
    # 감속일 경우
    elif user_input == 2:
        speed -= 10
        if speed < 0:
            print("속도는 음수일수가 없습니다. 뒤로 갈까요?")
            speed = 0
        else:
            print(f"현재 속도는 {speed}km!")
    else:
        print("다시 입력해주세요.")
