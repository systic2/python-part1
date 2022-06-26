# 사용자에게 명령어를 입력받아서 터틀그래픽을 제어해보자.
# 사용자가 "left"를 입력하면 왼쪽으로 회전
# 사용자가 "right"를 입력하면 오른쪽으로 회전

import turtle
# 펜의 기능을 t라는 변수에 저장
t = turtle.Pen()
# 반복문을 무한루프를 돌려서 if 구문을 이용하여 방향을 제어하는 코드
# 무한루프를 프로그래밍을 했다면 반드시 루프를 탈출하는 코드가 반드시 있어야 한다.(중요)
while True:
    direction = input("왼쪽은 left, 오른쪽은 right, 종료는 quit : ")
    # break 는 무한루프를 빠져나가라는 키워드이다.
    if direction == "quit":
        print("종료되었습니다.")
        break
    # 사용자가 left를 입력했을때
    if direction == "left":
        print("left")
        t.left(60)
        t.forward(50)
    # 사용자가 left를 입력했을때
    if direction == "right":
        print("right")
        t.right(60)
        t.forward(50)

# 터틀 그래픽 창이 클릭이 되어야 화면에서 사라지게 하는 코드
turtle.exitonclick()