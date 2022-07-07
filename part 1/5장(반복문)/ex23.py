# 사용자로부터 전화번호를 입력받다 보면 "-"를 적는 경우가 많다.
# "-"을 합하여 입력받도록 하고 출력을 할 때는 "-" 삭제를 한 문자열을 출력하는 프로그램

phone_num = input("전화번호를 입력하세요 : ")

real_num = ''

if len(phone_num) == 12 or len(phone_num) == 13:
    for digit in phone_num:
        if digit.isdigit():
            real_num += digit

    print(f"입력하신 번호는 {real_num} 입니다.")

else:
    print("전화번호 입력이 잘못되었습니다.")
