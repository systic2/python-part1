# 정렬하기에 대한 실습
list1 = [4, 8, 9, -1, 10]
# 리스트 객체에서 제공해주는 sort()를 이용하여 정렬하는 방법
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)


# 선택 정렬 알고리즘을 통한 정렬하기
# 선택 정렬이라는 방식은 주어진 리스트 중에서 일단 최소값을 찾는다.
# 그 최소값을 맨 앞에 위치한 값과 교환한다.
# 맨 처음 위치를 뺀 나머지 리스트를 위와 똑같은 방법으로 루핑하면서 최종적으로 정렬이 이루어진다.
# 선택 정렬은 제자리 정렬이기 때문에 더블루프를 사용해야 한다.
def selectionSort(li):
    cnt = 0
    for i in range(len(li) - 1):
        min_idx = i
        for j in range(i + 1, len(li)):
            if li[min_idx] > li[j]:
                min_idx = j

        if min_idx != i:  # 최소값을 찾았다면
            # 두 인덱스의 해당하는 값을 서로 바꾼다
            print(li[i], li[min_idx], "을 교환합니다.")
            li[i], li[min_idx] = li[min_idx], li[i]
            print(li[i], li[min_idx], "을 교환한 결과입니다.")
            cnt += 1

    print(cnt, "만큼 교환이 이루어졌습니다.")
    return li


# 버블 정렬 알고리즘
# 인접한 두 원소를 검사하여 정렬하는 방법인데 정확도는 높다.
# 데이터가 많아지면 많아질수록 속도가 떨어진다.

def bubble_sort(li):
    list_length = len(li)
    for i in range(list_length - 1):
        for j in range(list_length - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


if __name__ == "__main__":
    li = [4, 6, 1, 10, 7, -7, -100, 15, 30, 5]
    selectionSort(li)
    print(li)
    print("---------------------------")
    li = [4, 6, 1, 10, 7, -7, -100, 15, 30, 5]
    bubble_sort(li)
    print(li)
