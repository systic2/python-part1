# 내장함수를 이용한 문제 해결
# 초대받는 사람의 이름을 리스트로 만들었다.
names = ["신은혁", "김연아", "손연재", "손아섭"]
# 초대받은 사람과 동행하는 사람의 숫자를 리스트로 만들었다.
persons = [1, 3, 0, 6]

# 파티의 총 인원을 구하기
all_persons = len(names) + sum(persons)
print(f"파티 총 인원 : {all_persons}")

# 파티에 한 사람이라도 오는지를 확인하는 방법
# any() 함수를 이용하여 확인하면 된다.
isParty = any(persons)
print(f"파티에 한 사람이라도 오는가? : {isParty}")

# 모든 초대받은 그룹이 전부 오는지를 확인하는 방법
# all() 함수를 이용하여 확인하면 된다.
isComingAll = all(persons)
print(f"모든 초대받은 그룹이 전부 오는가? : {isComingAll}")

# 가장 많이 오는 그룹에는 몇 사람이나 있는지 확인하는 방법
# max() 함수를 이용하면 된다.
max_persons = max(persons)
print(f"가장 많이 오는 그룹은 몇 명인가? : {max_persons}명")

# 초대받은 사람과 동행하는 사람 수를 묶어서 출력해보기
# for 문과 zip() 함수를 이용하면 된다.
# matching_persons = zip(names, persons)
# print(f"초대받은 사람과 동행하는 사람 수 : {list(matching_persons)}")
for name, person in zip(names, persons):
    print(name, person)