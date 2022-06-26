# 피보나치 수열을 구하는 프로그램
# 피보나치 수열이란 앞의 두 수를 더해서 다음 수를 결정짓는 수열
# 예) 13까지의 피보나치 수열의 값 : 1 1 2 3 5 8

num = int(input("정수를 입력하세요 : "))

# p = 1
# first = 0
# second = 1
# while True:
#     if p >= num:
#         break
#     p = first + second
#     first = second
#     second = p
#     print(p, end=" ")

n3 = 1
n1 = 1
n2 = 1

for i in range(1, num):
    if i < 3:
        n3 = 1
    else:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    # 사용자로부터 입력받은 값보다 작은 수만 출력하게끔 함
    if n3 < num:
        print(n3, end=" ")
