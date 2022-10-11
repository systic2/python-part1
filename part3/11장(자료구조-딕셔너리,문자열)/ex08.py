# 문제
# 문자열 안에 있는 문자의 개수, 숫자의 개수, 공백의 개수를 계산하는 프로그램을 작성
# 출력결과
# 문자열을 입력하시오 : A picture is worth a thousand words.
# {'digits': 0, "spaces" : 6, 'alphas': 29}

# string = input("문자열을 입력하세요 : ")
# digits = 0
# spaces = 0
# alphas = 0
# for ch in string:
#     if ch.isdigit():
#         digits += 1
#     elif ch.isspace():
#         spaces += 1
#     elif ch.isalpha():
#         alphas += 1
# result = {
#     'digits': digits,
#     'spaces': spaces,
#     'alphas': alphas,
# }
#
# print(result)

def main():
    string = input("문자열을 입력하세요 : ")
    dic1 = {"alphas": 0, "digits": 0, "spaces": 0}
    for i in string:
        # 알파벳이라면..
        if i.isalpha():
            dic1["alphas"] += 1
        if i.isdigit():
            dic1["digits"] += 1
        if i.isspace():
            dic1["spaces"] += 1

    print(dic1)


if __name__ == "__main__":
    main()
