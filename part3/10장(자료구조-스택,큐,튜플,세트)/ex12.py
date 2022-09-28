# 문제 : 텍스트 파일을 읽어서 단어를 얼마나 다양하게 사용하여 문서를 작성하였는지를 계산하는 프로그램을 작성하시오.
# 출력결과
# 입력 파일 이름 : word.txt
# 사용된 단어의 개수 : 18

# with open('words.txt', 'r') as f:
#     words_list = f.read()
#     words = words_list.split(' ')
#     set_words = set(words)
#     print(f'사용한 단어의 개수 : {len(set_words)}')
#     print(f'{set_words}')

# 단어에서 마침표를 제거하고 소문자로 만드는 함수
def process(word):
    out_str = ""
    for ch in word:
        if ch.isalpha():  # 영문자라면
            out_str += ch
    return out_str.lower()


if __name__ == '__main__':
    words = set()   # 비어있는 세트를 만든다.
    f_name = input("입력 파일 이름 : ")
    file = open(f_name, mode='r')   # 파일을 열고 읽기 모드로 설정

    # 파일의 모든 줄에 대해서 반복한다.
    for line in file:
        lineWords = line.split()  # 한 라인을 읽어와서 단어(토큰)별로 분리하고 있다.
        for word in lineWords:
            words.add(process(word))     # 단어를 세트에 추가한다.

    print(f'사용한 단어의 개수 : {len(words)}')
    print(f'{words}')
    file.close()