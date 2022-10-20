# 일반 딕셔너리를 정렬을 하여 OrderedDict 로 포장하기
dic = {}
dic["b"] = 100
dic["a"] = 200
dic["d"] = 300
dic["c"] = 400
dic["e"] = 500
# 키의 값으로 정렬
li1 = sorted(dic.keys())
li2 = sorted(dic.values())
print(li1)
print(li2)
print(dic["c"])

from collections import OrderedDict

# 넘어오는 t의 값은 딕셔너리의 요소이다.
# 하여 0 인덱스는 key 값이 될 것이다. 1 인덱스는 value 값이 될 것이다.
def sort_by_key(t):
    return t[1]

dic1 = OrderedDict()
dic1["b"] = 100
dic1["a"] = 200
dic1["d"] = 300
dic1["c"] = 400
dic1["e"] = 500

# print(sorted(dic1.items(), key=sort_by_key))
# 일반 딕셔너리의 내용을 sorted() 를 이용하여 정렬을 하면 키를 기준으로 정렬된 리스트가 리턴된다.
# OrderedDict() 로 포장(wrapping) 을 하고 있다.
# 기존의 딕셔너리나 리스트의 순서를 지키면서 딕셔너리의 형태로 관리를 할 수 있다.
for k, v in OrderedDict(sorted(dic1.items(), key=sort_by_key)).items():
    print(k, v)

# 딕셔너리의 동등성 비교
