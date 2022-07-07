# 사용자로부터 문자열을 입력받아서 알파벳 문자의 개수, 숫자의 개수,
# 스페이스의 개수를 출력하는 프로그램을 작성
word = input("문자열을 입력하세요(영문자, 숫자, 공백) : ")
alphabet = 0
number = 0
space = 0
word = word.lower()
if len(word) > 0:
    for ch in word:
        if ch.isalpha():
            alphabet += 1
        elif ch.isdigit():
            number += 1
        elif ch.isspace():
            space += 1
        else:
            print("해당문자는 알파벳, 숫자, 공백이 아닙니다.")
            break

print(f'알파벳 : {alphabet}, 숫자 : {number}, 스페이스 : {space}')
