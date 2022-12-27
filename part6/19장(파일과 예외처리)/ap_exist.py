# 하나의 파일을 읽어서 그 안에 각 알파벳이 몇 개가 있는지 확인하는 프로그램 작성
counter = [0] * 26
infile = open("files/mobydick.txt", "r")
ch = infile.read(1)
while ch != "":
    ch = ch.upper()     # 대문자로 바꾼다.
    # 알파벳이라면...
    if ch >= "A" and ch <= "Z":
        # ord() 는 유니코드를 반환, A를 빼면 현재 알파벳의 문자번호를 알 수 있다.
        i = ord(ch) - ord("A")
        counter[i] += 1
    ch = infile.read(1)
print(counter)
