# 사용자로부터 연도를 입력받고 윤년인지 아닌지를 판단하는 프로그램
# 윤년의 조건
# 1. 연도가 4로 나누어 떨어지면 윤년
# 2. 100으로 나누어 떨어지는 연도는 제외
# 3. 400으로 나누어 떨어지는 연도는 윤년

year = int(input("연도를 입력하세요 : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"입력하신 {year}은 윤년입니다.")
        else:
            print(f"입력하신 {year}은 윤년이 아닙니다.")
    else:
        print(f"입력하신 {year}은 윤년입니다.")
else:
    print(f"입력하신 {year}은 윤년이 아닙니다.")

# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     print(f"입력하신 {year}은 윤년입니다.")
# else:
#     print(f"입력하신 {year}은 윤년이 아닙니다.")