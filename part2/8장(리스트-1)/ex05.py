# 인덱싱 : 리스트에서 하나의 요소를 인덱스를 통하여 참조하는 것
li = ["안녕", "신은혁", 10, 100, -10]
print(li[2])

# 음수 인덱스는 뒤에서부터 계산한다. 시작값은 -1이다.
#
print(li[-2])
print(li[-2 + len(li)])

# 슬라이싱(slicing) : 리스트 범위 안에서 범위를 지정하여 원하는 요소들을 선택하는 연산을 칭한다.
li1 = ["안녕", "신은혁", 10, 100, -10, False, True]
print("li1의 주소값 : ", id(li1))
# 인덱스의 값을 통해서 부분 리스트를 새로 만든다. (끝 인덱스는 제외함)
s_li1 = li1[2:6]
print("s_li1의 주소값 : ", id(s_li1))
print("s_li1 : ", s_li1)
# 슬라이싱 연산을 할 때, 앞의 인덱스가 생략되면 0부터 시작함을 이해하자.
s_li3 = li1[1:]
print("s_li3의 주소값 : ", id(s_li3))
print("s_li3 : ", s_li3)
# 아래 코드는 li1의 값ㅇ르 전부 출력한다.
print(li1[:])

# 슬라이싱을 통해 값을 변경하는 내용 실습
words = ["a", "b", "c", "d", "e"]
print("words 주소값 : ", id(words))
print("words : ", words)
words[1:3] = ["B", "C", "D"]
print("words 주소값 : ", id(words))
print(words)
# 아래 코드는 요소들이 다 삭제가 된다.
words[:] = []
print("words 주소값 : ", id(words))
print(words)
