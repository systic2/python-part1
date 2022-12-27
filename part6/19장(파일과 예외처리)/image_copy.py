# 이미지 복사하기

# 모드가 rb, wb 라는 것은 이진 파일이라는 뜻이다.
infile = open("diamond.png", "rb")
outfile = open("diamond_copy.png", "wb")

while True:
    copy_buffer = infile.read(1024)
    if not copy_buffer:     # 파일의 끝이라면
        break
    outfile.write(copy_buffer)  # 복사될 이미지에 읽은 내용을 추가

infile.close()
outfile.close()
print("diamond.png를 diamond_copy.png로 복사하였습니다.")
