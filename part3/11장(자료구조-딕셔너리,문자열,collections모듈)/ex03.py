# 영한 사전 만들기
# 공백 딕셔너리 생성하고 여기에 영어단어를 키로 하고 설명을 값으로 저장하면 될 것이다.
# 출력결과
# 단어를 입력하시오 : one
# 하나
# 단어를 입력하시오 : python
# 해당하는 단어가 없습니다.
# -------------------------------------------------

def find_word(dic, word):
    if word in dic:
        return dic[word]
    else:
        return '해당하는 단어가 없습니다.'


if __name__ == "__main__":
    eng_kor_dict = dict()  # 빈 딕셔너리 생성
    # 빈 딕셔너리에 데이터를 추가하기
    eng_kor_dict["one"] = '하나'
    eng_kor_dict["two"] = '둘'
    eng_kor_dict["three"] = '셋'
    eng_kor_dict["four"] = '넷'
    eng_kor_dict["five"] = '다섯'
    user_input = input("단어를 입력하시오 : ")
    result = find_word(eng_kor_dict, user_input)
    print(result)
