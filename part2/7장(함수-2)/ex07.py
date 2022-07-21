# 지역변수와 전역변수 실습

# def test():
#     # UnboundLocalError: local variable 'text' referenced before assignment
#     # 함수 안에서 하나의 변수가 전역변수가 되었다가 다시 지역변수가 될 수가 없다.
#     # print(text)
#     text = "파이썬 공부"
#     print(text)
#
# text = "자바 공부"
# test()
# print(text)

# 전역변수를 함수 안에서 값을 변공하고자 한다면... global 키워드를 함수 안에 명시적으로 적어 줘야한다.

def test():
    # test() 함수 안에서 전역변수인 text를 사용하겠다라는 것을 인터프리터한테 알린다.
    global text
    print(text)
    text = "파이썬 공부"     # 전역변수의 값을 변경하고 있다.
    print(text)

text = "자바 공부"
print(text)  # 전역변수의 값이 변경되기 전에 출력
test()
print(text)  # 전역변수의 값이 변경된 후에 출력
