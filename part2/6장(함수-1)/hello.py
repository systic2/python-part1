def say_hello_name(name):  # 함수의 선언부(헤더)
    print("안녕하세요, " + name)  # 함수의 구현부(정의부, 몸체)

def say_hello_name_msg(name, msg):  # 함수의 선언부(헤더)
    print("안녕하세요, " + name, msg)  # 함수의 구현부(정의부, 몸체)

# 값을 반환하는 함수 예제
# start부터 end까지의 합을 구하는 함수
def get_sum(start, end):
    hap = 0
    for i in range(start, end+1):
        hap += i
    return hap
