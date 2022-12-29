# 문제1
# random 모듈에 있는 함수를 사용해서 7개의 단어 중에서 랜덤하게 3개를 선택하여 출력하는 프로그램
import random
words = []
words.append("파이썬")
words.append("C언어")
words.append("학습")
words.append("프로그램")
words.append("코딩")
words.append("마우스")
words.append("컴퓨터")
# print(words)
# -------------------------------------------
# first = random.choice(words)
# print(first)
# words.remove(first)
# second = random.choice(words)
# print(second)
# words.remove(second)
# third = random.choice(words)
# print(third)

# 풀이
result = ""
for i in range(0, 3):
    result += random.choice(words) + " "

print(f"추출한 word 3개 : {result}")
print("--------------------------------------")

# 문제2
# random 모듈에 있는 함수를 사용해서 알파벳 a부터 z 사이에서 램덤하게 10개의 문자를 출력하는 프로그램
str1 = "abcdefghijklmnopqrstuvwxyz"
# --------------------------------------------------------------------
result2 = []
i = 0
while i < 10:
    letter = random.choice(str1)
    if letter not in result2:
        result2.append(letter)
        i += 1
print(result2)
# 과제
# 중복된 알파벳은 제외하고 출력해보기
print("--------------------------------------")

# 문제3
# 100과 200 사이에서 5개의 짝수 난수를 발생시키는 프로그램을 작성(random.sample() 사용)
num_list = [x for x in random.sample(range(100, 201, 2), 5)]
print(num_list)
# 풀이
print("100~200 사이 짝수 난수 5개 : ", random.sample([i for i in range(100, 201) if i % 2 == 0], 5))
