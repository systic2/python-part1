# 중첩(nested) if ~ else 구문
# 사용자로부터 아이디를 입력받아서 등록되어진 아이디인지를 검사하는 프로그램을 작성하는데,
# 등록된 아이디를 리스트(list)에 저장하도록 한다.
# 아이디가 등록되어 있다면 패스워드를 물어보도록 한다.
# 단, 패스워드는 "1234"라고 가정하도록 한다.

list_in_id = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
pwd = "1234"
user_id = input("아이디를 입력하세요 : ")


if user_id not in list_in_id:     # 사용자가 입력한 id가 list에 존재하지 않는다면
    print("회원가입하세요")
else:                               # 사용자가 입력한 id가 list에 존재한다면
    user_pwd = input("비밀번호를 입력하세요 : ")
    if user_pwd == pwd:               # 사용자가 입력한 pwd가 1234와 일치한다면
        print(f"{user_id}님 환영합니다.")
    else:                           # 일치하지 않는다면
        print("비밀번호가 틀렸습니다!")