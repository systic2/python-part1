# 사용자로부터 태어난 연도를 입력받아서 초등학생, 중학생, 고등학생, 대학생 분류 중에서
# 어디에 해당하는지를 출력하는 프로그램을 작성
# 나이 : 8 ~ 13(초등학생), 14~16(중학생), 17~19(고등학생), 20~27(대학생) 이외 나이는 일반인으로 분류

current_year = 2022
birth_year = int(input("태어난 연도를 입력해주세요 : "))

age = current_year - birth_year + 1 # 우리나라 나이 계산
print(age)
if 8 <= age <= 13: # (age >= 8) and (age <= 13)
    print("초등학생")
elif 14 <= age <= 16:
    print("중학생")
elif 17 <= age <= 19:
    print("고등학생")
elif 20 <= age <= 27:
    print("대학생")
elif age < 8:
    print("유아")
else:
    print("일반인")