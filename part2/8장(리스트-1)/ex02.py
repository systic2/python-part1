# 학생들의 성적을 처리하는 프로그램 만들기
# 조건 : 사용자로부터 성적을 입력받아서 리스트에 저장
# 성적의 평균을 구하고 해당 점수가 80점 이상 성적을 받은 학생의 수를 출력
# 출력결과
# 성적을 입력하시오 : 10
# 성적을 입력하시오 : 20
# 성적을 입력하시오 : 60
# 성적을 입력하시오 : 70
# 성적을 입력하시오 : 80

scores = []
result = 0
total = 0
count = int(input("학생 수를 입력하세요 : "))
for i in range(count):
    scores.append(int(input("성적을 입력하세요 : ")))
    if scores[i] >= 80:
        result += 1
    total += scores[i]
avg = round((total / count), 1)
print(f"성적 평균은 {avg} 입니다.")
print(f"80점 이상 성적을 받은 학생은 {result} 입니다.")

print("-" * 50)

STUDENT = 5  # 전역 상수 선언
scores = []  # 학생들의 성적을 저장할 리스트
score_Sum = 0  # 학생들의 성적 합계를 저장할 변수
score_aver = 0.0   # 학생들의 성적 평균을 저장할 변수
cnt_80 = 0  # 80점 이상인 학생 수 합계를 저장할 변수

for i in range(STUDENT):
    score = int(input("성적을 입력하세요 : "))
    scores.append(score)  # 학생들의 성적을 list에 저장함(append() 이용)
    score_Sum += score  # 성적 합계
    # 80점 이상 학생수 구하기
    if score >= 80:
        cnt_80 += 1

score_aver = score_Sum / len(scores)  # 평균을 구함

print("성적 평균은", score_aver, "입니다.")
print("80점 이상 성적을 받은 학생은", cnt_80, "명입니다.")

