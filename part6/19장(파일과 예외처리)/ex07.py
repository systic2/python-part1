# for 문
# infile = open("input.txt", "r")
# for line in infile:
#     print(line)

# 단어를 분리하기
# infile = open("proverbs.txt", "r")
# for line in infile:
#     line = line.rstrip()    # 오른쪽 공백 문자를 제거
#     word_list = line.split()    # 단어들 분리
#     for word in word_list:
#         print(word)
#
# infile.close()

# 구분자를 지정해서 단어를 출력
# line = "apple,grape,banana,pear"
# word_list = line.split(",")     # 구분자를 통한 리스트 반환
# for word in word_list:
#     print(word)

# 1문자씩 출력하기
infile = open("files/input.txt", "r")
ch = infile.read(1)
while ch != "":
    print(ch)
    ch = infile.read(1)
infile.close()
