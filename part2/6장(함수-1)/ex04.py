# 섭씨 온도를 화씨 온도로 변환하여 반환하는 함수 CtoF()를 작성
# 공식 : 화씨 = (9.0/5.0)*섭씨+32

def CtoF(C):
    F = ((9.0/5.0)*C)+32
    return F

C = float(input("섭씨온도를 입력해주세요 : "))
F = round(CtoF(C), 1)

print(f'입력한 섭씨는 {C}이고 변환된 화씨는 {F}도 입니다.')

def FtoC(temp_f):
    temp_c = (5.0* (temp_f - 32))/9.0
    return temp_c

temp_f = float(input("화씨온도를 입력해주세요 : "))
temp_c = round(FtoC(temp_f), 1)
print(f'입력한 화씨는 {temp_f}이고 변환된 화씨는 {temp_c}도 입니다.')