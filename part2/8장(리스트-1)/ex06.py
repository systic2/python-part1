# 리스트의 기초 연산들 실습하기

# 리스트에 요소 삽입하기
# append() 메서드 : 리스트명.append(추가할 요소) 리스트 요소의 항상 마지막 끝에 추가된다.
# insert() 메서드 : 리스트명.insert(인덱스, 추가할 요소) 원하는 인덱스에 요소를 추가할 수 있다.

li1 = ['TV', '오디오', 'PC', '키보드']
print('li1의 주소 : ', id(li1))
print(li1)
# append() 사용
li1.append("마우스")
print("li1의 주소 : ", id(li1))
print(li1)
# insert() 사용하여 원하는 인덱스에 요소 추가, 뒤에 요소들이 한 칸씩 밀려났다.
li1.insert(1, "휴대폰")
print("li1의 주소 : ", id(li1))
print(li1)

# 리스트에서 요소 찾기
# in, not in 연산자들은 리스트에 요소가 존재하는지 확인하는 용도

heros = ["스파이더맨", "배트맨", "슈퍼맨", "아이언맨", "헐크", "홍당무"]
if "배트맨" in heros:
    print("배트맨이 존재합니다.")
else:
    print("배트맨이 존재하지 않습니다.")

# 리스트에서 요소를 찾을 때 해당 요소의 인덱스를 알고자 한다면 index()를 사용하면 된다.
# 아래와 같이 list에 해당하는 값이 존재하지 않으면 index()는 에러를 발생시킨다.
# 그러므로, 조건절과 in, not in 연산자를 이용하여 존재하는지 확인을 먼저 하는 습관을 들이도록 한다.
if "홍당무" in heros:
    index = heros.index("슈퍼맨")
    print("슈퍼맨의 인덱스 : ", index)
else:
    print("홍당무가 존재하지 않습니다.")

# 리스트에서 요소를 삭제하는 방법
# 1 : 리스트명.pop(인덱스), 리스트에서 인덱스에 해당하는 요소를 삭제한 후, 요소를 반환한다.
# 2 : 리스트명.remove("요소"), 리스트에서 해당하는 요소가 있으면 삭제한 후, 요소를 반환 안한다.
# 3 : del 리스트명[인덱스], 리스트에서 인덱스에 해당하는 요소를 삭제한 후, 요소를 반환 안한다.

heros = ["스파이더맨", "배트맨", "슈퍼맨", "아이언맨", "헐크", "태권V", "배트맨"]
element = heros.pop(0)
print("element : ", element)
print(heros)

# remove() 메서드는 리스트의 요소 중 중복된 요소가 존재한다면 인덱스가 작은 요소를 먼저 제거를 한다.
value = "배트맨"
while value in heros:
    heros.remove(value)

print(heros)

# del 키워드로 요소를 삭제하기
heros = ["스파이더맨", "배트맨", "슈퍼맨", "아이언맨", "헐크", "태권V", "배트맨"]
del heros[:]
print(heros)

# 리스트의 모든 요소를 삭제를 하고자 한다면, 리스트명.clear() 사용하면 된다.
heros = ["스파이더맨", "배트맨", "슈퍼맨", "아이언맨", "헐크", "태권V", "배트맨"]
element = heros.clear()
print(heros)
print(heros)
