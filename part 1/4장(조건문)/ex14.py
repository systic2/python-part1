# 몸무게와 키를 입력받고 BMI가 20.0 이상이고 25미만이면
# 표준입니다 라고 출력을 하고 아니면 체중관리가 필요합니다 라고 출력하는 프로그램
# BMI = 몸무게 / (키 * 키)

height = float(input("키를 입력하세요(cm) : "))
weight = float(input("몸무게를 입력하세요(kg) : "))
# 복합대입 연산자 이용
height /= 100.0 # height = height / 100.0

BMI = weight / (height * height)
print("BMI 값 : ", BMI)

if BMI >= 20.0 and BMI < 25.0:
    print("표준입니다.")
else:
    print("체중관리가 필요합니다.")