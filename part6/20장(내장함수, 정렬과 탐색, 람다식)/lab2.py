# 내장함수를 이용한 문제 해결 - 2
# 1. 리스트 함축과 내장함수를 이용하여 1~100까지의 정수 중에서 3의 배수의 개수 세기
# times_number_3 = [x for x in range(1, 101) if x % 3 == 0]
# print(len(times_number_3))

count = sum([1 for k in range(1, 101) if k % 3 == 0])
print(f"1~100까지의 3의 배수 개수 : {count}")

# 2. 내장함수를 이용하여 사용자가 어떤 문자열을 입력하더라도 오류를 일으키지 아니하고
# 정수나 실수로 변환하는 코드를 작성해보자
n = eval(input("정수나 실수를 입력하시오 : "))
print("입력된 정수나 실수의 값 : ", n)
