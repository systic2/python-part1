# 문제3
# 문장의 한 단어의 빈도수를 계산하여 DB에 저장하고 출력하는 프로그램을 작성하시오.
# 인용할 문장 :
"""
같이 다하지 없이 별에도 어머니 못했던 가난한 이웃 버리었습니다.
어머님, 위에도 많은 언덕 봄이 버리었습니다. 이름과, 풀이 프랑시스 흙으로 다 헤는 쉬이 듯합니다.
위에 흙으로 잔디가 별에도 동경과 쉬이 까닭이요, 내 있습니다.
무엇인지 별을 덮어 계십니다. 별 쉬이 토끼, 때 청춘이 있습니다.
계집애들의 별 이름과 나의 위에도 나는 내 가을로 언덕 계십니다.
마리아 언덕 이웃 봅니다. 하나에 청춘이 노루, 까닭입니다.
벌레는 강아지, 하나에 청춘이 계십니다. 하나에 이름을 흙으로 가을 보고,
별들을 나는 봅니다.
"""
# 단어    빈도수
# ------------
# 같      1
# 이      4
# ------------
import sqlite3

con, cur = None, None
word, frequency = "", ""
string = """
같이 다하지 없이 별에도 어머니 못했던 가난한 이웃 버리었습니다.
어머님, 위에도 많은 언덕 봄이 버리었습니다. 이름과, 풀이 프랑시스 흙으로 다 헤는 쉬이 듯합니다.
위에 흙으로 잔디가 별에도 동경과 쉬이 까닭이요, 내 있습니다.
무엇인지 별을 덮어 계십니다. 별 쉬이 토끼, 때 청춘이 있습니다.
계집애들의 별 이름과 나의 위에도 나는 내 가을로 언덕 계십니다.
마리아 언덕 이웃 봅니다. 하나에 청춘이 노루, 까닭입니다.
벌레는 강아지, 하나에 청춘이 계십니다. 하나에 이름을 흙으로 가을 보고,
별들을 나는 봅니다.
"""


if __name__ == '__main__':
    con = sqlite3.connect("/Users/systic/Desktop/sqlite/naverDB")
    cur = con.cursor()
    cur.execute("drop table if exists wordTable")
    cur.execute("create table wordTable(word char(4) primary key, frequency int)")

    string_list = list(string.strip())
    string_dict = {}
    for char in string_list:
        if char in [" ", ",", ".", "\n"]:
            continue

        if char in string_dict.keys():
            string_dict[char] += 1
        else:
            string_dict[char] = 1

    # print(string_dict)
    for key, value in string_dict.items():
        cur.execute("insert into wordTable(word, frequency) values(?, ?)", (key, value))

    con.commit()

    cur.execute("select * from wordTable order by frequency desc")

    print("단어   빈도수")
    print("-----------")

    while True:
        row = cur.fetchone()
        if row is None:
            break
        word = row[0]
        frequency = row[1]
        print(f"{word:4s} {frequency:2d}")

    con.close()
