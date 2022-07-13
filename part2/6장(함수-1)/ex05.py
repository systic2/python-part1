# 사용자로부터 정수를 입력받아서 소수를 판변하는 함수 is_prime()을 작성해보자
# 소수면 True, 소수가 아니면 False 출력

def is_prime(num):
    result = False
    if num <= 2:
        return result
    for i in range(2, num):
        if num % i != 0:
            result = True
        else:
            result = False
            return result
    return result

num = int(input("정수를 입력하세요 : "))
result = is_prime(num)

print(f'입력하신 정수는 {num}이고 소수 여부는 {result}입니다.')