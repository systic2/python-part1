# mutable object 중 dictionary 라는 타입이 있다
# 딕셔너리라는 타입 형태는 키와 값의 쌍으로 이루어져 있다
# 딕셔너리의 키의 값은 유니크한 값이 되어야 한다. 하지만 값은 변경이 가능

def change(dic):
    print("change()함수 내의 연산 전 dic 값 : ", dic)
    print("change()함수 내의 연산 전 dic 주소 값 : ", id(dic))
    dic["몸무게"] = 42
    print("change()함수 내의 연산 후 li 값 : ", dic)
    print("change()함수 내의 연산 후 li 주소 값 : ", id(dic))


dic = {"name": "신은혁", "age": 14, "height": 160}
print(dic)
# 키를 주고 값을 얻어온다
# print(dic["name"])
print("호출 전의 list 값 : ", dic)
print("호출 전의 list 주소 값 : ", id(dic))
change(dic)
print("호출 후의 list 값 : ", dic)
print("호출 후의 list 주소 값 : ", id(dic))
