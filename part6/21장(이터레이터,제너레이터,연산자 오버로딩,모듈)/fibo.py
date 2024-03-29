# 모듈에 대한 실습
# 모듈 : 파이썬에서는 모듈(module)은 변수나 함수, 그리고 클래스들을 모아 놓은 파일
# 모듈은 확장자가 반드시 .py 가 되어야 한다.
# 모듈을 사용하는 이유가 유지보수를 쉽게 하기 위해서 여러 개의 파일로 분리할 수 있다.
# 또한 모듈에 정의 및 구현해놓은 함수를 따로 작성하지 아니하고 가져다 여러 프로그램에서 사용하면 된다.
# 이것이 바로 코드의 재활용이다.
# 모듈을 사용하기 위해서는 import 키워드를 사용하여 모듈을 파일로 가져오면 된다.

# 피보나치 수열 모듈 만들기
# 정수 형태로 피보나치 수열을 출력하는 함수
def fib_num(n):
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a + b
    print()


# 리스트 형태로 피보나치 수열을 출력하는 함수
def fib_list(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)  # 순차적으로 리스트에 b 값을 추가
        a, b = b, a + b
    return result
