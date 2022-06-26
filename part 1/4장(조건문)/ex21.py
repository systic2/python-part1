# 학점을 세부적으로 나누는 프로그램 작성(중첩 if 문 사용)
# 조건
# 1. 사용자로부터 점수를 입력
# 2. 점수가 95이상 100이하라면 A+ 을 출력
# 3. 점수가 90이상 94이하라면 A0를 출력
# 다른 B, C, D 학점도 위와 같이 출력
# 단, F는 그냥 출력

score = int(input("점수를 입력하세요(0~100)[점] : "))
print(f"입력하신 점수는 {score}점입니다.")

print("-" * 50)
print("계산 결과")
print("-" * 50)

if 90 <= score <= 100:
    if score >= 97:
        print("A+ 학점입니다.")
    elif 94 <= score < 97:
        print("A0 학점입니다.")
    else:
        print("A- 학점입니다.")
elif 80 <= score < 90:
    if score >= 87:
        print("B+ 학점입니다.")
    elif 84 <= score < 87:
        print("B0 학점입니다.")
    else:
        print("B- 학점입니다.")
elif 70 <= score < 80:
    if score >= 77:
        print("C+ 학점입니다.")
    elif 74 <= score < 77:
        print("C0 학점입니다.")
    else:
        print("C- 학점입니다.")
elif 60 <= score < 70:
    if score >= 67:
        print("D+ 학점입니다.")
    elif 64 <= score < 67:
        print("D0 학점입니다.")
    else:
        print("D- 학점입니다.")
else:
    print("F 학점입니다.")

