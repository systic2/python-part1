# 연락처 관리 프로그램 만들기
# 출력결과
# -------------------------
# 1. 친구 리스트 출력
# 2. 친구추가
# 3. 친구삭제
# 4. 이름변경
# 9. 종료
# 메뉴를 선택하시오: 2
# 이름을 입력하시오: 홍길동
# ------------------------
# 1. 친구 리스트 출력
# 2. 친구추가
# 3. 친구삭제
# 4. 이름변경
# 9. 종료
# 메뉴를 선택하시오: 1
# ['홍길동']

def menu_print():
    print('-----------------------')
    print('1. 친구 리스트 출력')
    print('2. 친구추가')
    print('3. 친구삭제')
    print('4. 이름변경')
    print('9. 종료')


friends_list = []  # 친구 목록 선언
menu_num = 0
while True:
    menu_print()
    menu_num = int(input("메뉴를 선택하시오 : "))

    if menu_num == 9:
        print("종료되었습니다.")
        break
    elif menu_num == 1:
        print(friends_list)
    elif menu_num == 2:
        newFriend = input('추가할 이름을 입력하시오 : ')
        friends_list.append(newFriend)
    elif menu_num == 3:
        deletefriend = input('삭제할 이름을 입력하시오 : ')
        if deletefriend in friends_list:
            friends_list.remove(deletefriend)
            print(deletefriend, '님이 삭제되었습니다.')
        else:
            print(deletefriend, "님이 존재하지 않습니다.")
    elif menu_num == 4:
        oldfriend = input('바꿀 이름을 입력하시오 : ')
        if oldfriend in friends_list:
            editindex = friends_list.index(oldfriend)
            editfriend = input('새로운 이름을 입력하시오 : ')
            friends_list[editindex] = editfriend
        else:
            print(oldfriend, '님이 존재하지 않습니다.')

# 친구 추가 시 연락처도 함께 추가하는 프로그램으로 업데이트 해보기



