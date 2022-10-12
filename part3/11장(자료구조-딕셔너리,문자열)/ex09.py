# 문제
# 머리 글자어(acronym)은 NATO(North Atlantic Treaty Organization)처럼
# 각 단어의 첫 글자를 모아서 만든 문자열이다.
# 사용자로부터 문장을 입력하면 해당되는 머리 글자어를 출력하는 프로그램을 만들어보자.

def make_acronym(s):
    result = ''
    words = s.split(' ')
    for word in words:
        result += word[0].upper()
    return result


if __name__ == "__main__":
    string = input("문자열을 입력하세요 : ")
    print("머리문자열 :", make_acronym(string))
