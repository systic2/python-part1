# 리스트는 다양한 데이터를 저장할 수 있다고 배웠다.
# 하지만 현업에서는 같은 종류(모델)의 같은 타입의 데이터를 저장하면서 사용한다.

# 리스트는 문자열도 저장할 수가 있다. 강아지를 많이 키우는 사람이 있다고 가정하자.
# 사용자로부터 강아지들의 이름을 저장하였다가 출력하는 프로그램을 작성해보라
# 조건 : 무한루프를 돌면서 엔터키가 입력이 되면 무한루프를 탈출한다.

dogs = []
dogname = ''
# 무한루프
while True:
    dogname = input("강아지의 이름을 입력하시오(종료시에는 엔터키) : ")
    if dogname == '':
        break
    else:
        dogs.append(dogname)

print(f"강아지들의 이름은 {dogs} 입니다.")