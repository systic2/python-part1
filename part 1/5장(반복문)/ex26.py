statements = "             안녕!                   "

# 왼쪽 공백만 제거하는 함수
print("제거전 문자열 :", statements)
print("왼쪽 공백 제거 :", statements.lstrip())


statements = "             안녕!                   "
print("제거전 문자열 :", statements)
print("오른쪽 공백 제거 :", statements.rstrip())

statements = "             안녕!                   "
print("제거전 문자열 :", statements)
print("양쪽 공백 제거 :", statements.strip())

# 문자열 나누기
statements = "나는 열심히 파이썬 공부를 합니다."
print(statements.split(' '))

