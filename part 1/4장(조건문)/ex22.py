# 사용자로부터 월을 입력받아서 입력한 월의 일수를 구하는 프로그램 작성

month = int(input("월을 입력하세요 : "))

if month == 2:
    print(f"{month}월의 일수는 28일")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(f"{month}월의 일수는 30일")
else:
    print(f"{month}월의 일수는 31일")