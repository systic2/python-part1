# 함수(function)에 대한 실습
# 1. 함수는 프로그램 안에서 중복된 코드를 제거한다
# 2. 복잡한 프로그래밍 작업을 더 간단한 작업들로 분해할 수 있다.
# 3. 함수는 한 번 만들어두면 재사용이 얼마든지 가능하다.
# 4. 함수를 사용하면 가독성이 증대되고, 유지관리도 쉬워진다.

# hello 파일의 내용을 전부 다 가져오기 때문에 파일이름.함수명으로 접근할 필요가 없고 함수명만 호출하면 된다.
# import hello
# 파일명.함수명으로 접근해야 한다.
import hello



# 간단한 함수
# def 키워드 함수이름(매개변수)
# def say_hello(name):  # 함수의 선언부(헤더)
#     print("안녕하세요, " + name)  # 함수의 구현부(정의부, 몸체)


# 위와 같이 함수를 정의만 했다면 출력값은 없다. 울력값이 나오게 할려면 호출(call) 해야한다.
# 함수 호출(function call)
hello.say_hello_name("신은혁")
hello.say_hello_name("홍길동")
# 함수가 호출되어 10을 출력하긴 하지만 가독성이 좋지 않다.
# 이유는 함수의 매개변수명이 name이니 웬만하면 이름을 매개변수 값으로 주는 것이 현명한 코드
# say_hello(10)

# 파이썬에서는 오버로딩의 개념이 없다. 같은 함수의 이름이라면 마지막에 정의되어진
# 함수만 인식하게 된다. 하여, 함수명은 유니크한 값으로 함수명을 짓도록 한다.
# def say_hello(name, msg):  # 함수의 선언부(헤더)
#     print("안녕하세요, " + name, msg)  # 함수의 구현부(정의부, 몸체)

hello.say_hello_name_msg("신은혁", "반갑습니다.")
hello.say_hello_name_msg("홍길동", "도와주세요.")


result = hello.get_sum(1, 10)
print(result, type(result))

result = hello.get_sum(1, 30)
print(result, type(result))

result = hello.get_sum(1, 100)
print(result, type(result))
