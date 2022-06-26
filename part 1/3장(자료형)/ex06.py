# 문자열의 인덱싱
# 인덱싱이란 문자열에서 문자를 추출하는데 문자열에는 각각에 해당하는 문자에 번호(인덱스)가 존재
# [인덱스] 하면 문자열에서 문자를 추출할 수 있다.
# 인덱스라 함은 무조건 0부터 시작이 된다. 마지막 인덱스는 n-1이 성립
# 파이썬 특수기능으로 인덱스를 처리할 때 음수도 사용이 가능하다.

word = "Python"
print(len(word))

print(word[0])
print(word[5])
# len(word)는 문자열의 길이인 6을 반환하므로 -1을 해주면 끝문자를 반환
print(word[len(word)-1])

# 해당 문자열의 인덱스의 범위 밖에 값을 주면 index out of range라는 에러가 발생
# print(word[100]) # IndexError: string index out of range

# 파이썬에서는 한 번 작성된 문자열은 변경이 불가능하다.
# word[2] = 'B' # TypeError

# 사용자로부터 문자열을 입력을 3개를 받도록 한다.
# 각 해당 문자열의 첫 번째 문자를 인덱싱하여 문자들을 합쳐서 문자열로 만드는 프로그램

str1 = input("첫 번째 문자열 입력 :")
str2 = input("두 번째 문자열 입력 :")
str3 = input("세 번째 문자열 입력 :")

# 위의 3개의 문자열 중 첫 번째 단어만 추출하여 또다른 문자열을 만들고 있다.
simple_str = str1[0] + str2[0] + str3[0]

print(simple_str)
