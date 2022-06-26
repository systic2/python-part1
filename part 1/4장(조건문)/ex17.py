# 사용자로부터 정수를 입력받아서 음수, 0, 양수 중에 어떤 값인지를 출력하는 프로그램

number = int(input("정수를 입력해주세요 : "))

if number < 0:
    print("입력하신 정수는 음수입니다.")
elif number > 0:
    print("입력하신 정수는 양수입니다.")
else:
    print("입력하신 정수는 0 입니다.")