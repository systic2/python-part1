# 일반적인 리스트 연산들 실습
# 최소값 최대값을 구하는 알고리즘

# 아래 코드는 이미 앞서서 배운바 있다.
# 내장 함수를 이용하여 최소값 최대값을 구하는 코드이다.
num = [1, 5, -9, 100]
print("최소값 : ", min(num))
print("최대값 : ", max(num))

# 최대값과 최소값을 구하는 알고리즘은 상당히 중요한 개념이므로 아래의 코드를 이해하도록 하자.
prices = [1000, 3000, 500, 10000, 20000, 700]
# 먼저 prices[] 에 있는 0번째 인덱스 값을 변수에 저장을 한다.
lowPrice = prices[0]
# 이후, 루프를 돌면서 조건식으로 값이 작으면 해당하는 값을 lowPrice 변수에 재저장
for i in range(1, len(prices)):
    # 참이다라는 것은 prices[i]가 lowPrice 보다 작다는 의미
    # 조건절에서 부등호를 수정을 하면 최대값을 구할 수도 있다.
    if prices[i] < lowPrice:
        lowPrice = prices[i]

print('가장 싼 가격은 :', lowPrice)
print('------------------------')

# 문자열에서 가장 짧은 문자열을 구하는 알고리즘 코드
words = ['dog', 'cat', 'horse', "lion", "tiger", "elephant"]
words_han = ['안녕', '하이', '반갑습니다', "가세요", "오랜만입니다.", "가지마세요"]
# 문자열 리스트에서 min()는 제일 첫 글자가 아스키코드 중에서 가장 작은 단어를 반환해준다.
print('가장 짧은 단어 :', min(words))
print('가장 긴 단어 :', max(words))
print('가장 짧은 단어 :', min(words_han))
print('가장 긴 단어 :', max(words_han))

# 문자열에서 가장 짧은 문자열을 구하는 알고리즘 코드
shortest_word = words[0]
list_word = []
for i in range(1, len(words)):
    if len(words[i]) <= len(shortest_word):
        if len(words[i]) < len(shortest_word):
            list_word.clear()
            list_word.append(words[i])
        else:
            list_word.append(shortest_word)
            shortest_word = words[i]
            list_word.append(shortest_word)

print('가장 짧은 단어이거나 같은 단어들 :', list_word)
print('가장 짧은 단어 :', shortest_word)

for word in list_word:
    print("가장 짧은 단어 : ", word)

