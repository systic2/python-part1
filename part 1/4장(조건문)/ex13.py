# 대학교 졸업하려면 적어도 140학점을 이수해야 하고 평점은 2.0은 되어야 한다.
# 이것을 프로그램으로 만들어보자
# 사용자에게 이수 학점과 평점을 입력받아서 졸업 가능 여부를 확인하는 프로그램

complete_class = int(input("이수 학점을 입력하세요 : "))
avg_score = float(input("평점을 입력하세요 : "))

if complete_class >= 140 and avg_score >= 2.0:
    print("졸업이 가능합니다.")
else:
    print("졸업이 불가능합니다.")