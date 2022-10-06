# str 클래스의 메서드 실습
# split() : 문자열에서 단어(토큰)을 분리하고자 할 때 사용하는 메서드이다.
# 인자값으로 구분자(seperator)를 주게 되면 주어진 구분자로 문자열을 분리한다.
# 기본 인자값 공백이다.
string = "안녕 john 난 지금 학교 가고 있어"
li1 = string.split()  # 공백으로 분리
print(type(li1))
print(li1)

# split()은 구분자를 하나밖에 받지 않는다.
string = "안녕,john,난,지금,학교,가고,있어"
li2 = string.split(",")  # 콤마로 분리
print(type(li2))
print(li2)

# 정규표현식을 사용하기 위해서 regex 모듈을 인스톨 하자
import regex

string = "안녕/john,난|지금&학교,가고,있어"
li3 = regex.split("[/,|&]", string)  # 정규표현식으로 분리
print(type(li3))
print(li3)
print('----------------------------')
# 문자열을 검사
string = 'abcd'
print(string.isalpha())  # 문자열이 영문자인지 확인하는 코드

string = "12345"
print(string.isdigit())  # 문자열이 10진수인지 확인하는 코드
print(string.isdecimal())  # 문자열이 10진수인지 확인하는 코드
print('----------------------------')

string = "abcd12345"
print(string.isalnum())  # 문자열이 영문자, 숫자인지 동시에 확인하는 코드
print('----------------------------')
string = "½"
print(string.isnumeric())  # numeric 굉장히 넓은 의미인데, 숫자값 표현에 해당하는 문자열을 인정해준다.

# str 클래스에서 음수, 실수 판별하는 메서드는 없다.
print('----------------------------')
string = "    "
print(string.isspace())  # 공백인지 확인하는 것

# 부분 문자열 검색 실습
print('----------------------------')

