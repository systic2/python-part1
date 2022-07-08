# 입력받은 문자열을 거꾸로 출력하는 프로그램

statements = input("문자열을 입력하세요 : ")

result = ''
result1 = ''
result2 = ''

for ch in range(len(statements)-1, -1, -1):
    result += statements[ch]

print(result)

result1 = statements[::-1]  # 슬라이싱 스텝 -1
print(result1)

for ch in statements:
    result2 = ch + result2  # 역순으로 문자열을 더해준다
print(result2)

s_list = list(statements)
# reverse() 리스트를 역순으로 바꾸는 함수
s_list.reverse()
print("".join(s_list))

s1 = statements
# reversed() 문자열에만 역순으로 하는 함수
print("".join(reversed(s1)))
