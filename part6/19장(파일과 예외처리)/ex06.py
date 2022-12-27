# 파이썬 파일 현재 위치 확인 및 변경을 하는 실습
# tell() : 파일의 현재 위치를 확인할 때 사용한다.
# seek() : 파일의 현재 위치를 변경할 때 사용한다.
# seek(0) : 파일의 처음 위치로 돌아간다.

file = open("files/test2.txt", "r")
print(f"파일포인터의 현재 위치 : {file.tell()}")
print(file.read())
print(f"파일포인터의 현재 위치 : {file.tell()}")
print("------------------------------------")
file.seek(0)    # 맨 처음 위치로 돌아가게끔 하였다.
print(f"파일포인터의 현재 위치 : {file.tell()}")
file.seek(5)    # 파일의 5번째 위치로 임의로 가게끔 하였다.
print(f"파일포인터의 현재 위치 : {file.tell()}")
# 30바이트 반큼 읽어서 출력하시오. UTF-8에서는 한글이 3바이트로 인식을 하는데
# 이런 이유로 인해 start 인덱스를 0으로 설정을 하지 않으면 에러가 발생한다.
print(file.read(30))

file.close()
