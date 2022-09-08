# 성적 처리 프로그램 만들기(2차원 리스트를 이용)
# 주어진 성적
# scores = [
#     [100, 100, 100], [20, 20, 20], [30, 30, 30],
#     [40, 40, 40], [50, 50, 50]
# ]
# 출력결과
# 번호  국어  영어  수학  총점  평균
# -----------------------------
# 1   100 100 100 300 100.00
# 2   20  20  20  60  20.00
# 3   30  30  30  90  30.00
# 4   40  40  40  120 40.00
# 5   50  50  50  150 50.00
# -----------------------------
# 총점  240 240 240 720 48.00


def subjectSum(li, idx):
    hap = 0
    for i in range(len(li)):
        hap += li[i][idx]
    return hap


def allSum(li):
    hap = 0
    for i in range(len(li)):
        hap += sum(li[i])
    return hap


def allCount(li):
    count = 0
    for i in range(len(li)):
        count += len(li[i])
    return count


scores = [
    [100, 100, 100], [20, 20, 20], [30, 30, 30],
    [40, 40, 40], [50, 50, 50]
]
print('번호\t국어\t영어\t수학\t총점\t평균')
print('--------------------------')
for i in range(len(scores)):
    print(f'{i+1}', end='\t')
    for j in range(len(scores[i])):
        print(f'{scores[i][j]}', end='\t')
    print(f'{sum(scores[i])}\t{sum(scores[i])/len(scores[i])}')
print('--------------------------')
print('총점', end='\t')
print(f'{subjectSum(scores, 0)}\t{subjectSum(scores, 1)}\t{subjectSum(scores, 2)}\t{allSum(scores)}\t{allSum(scores)/allCount(scores)}')

korTotal = 0
engTotal = 0
mathTotal = 0

allTotal =0
allAvg = 0.0
print('번호\t국어\t영어\t수학\t총점\t평균')
print('--------------------------')

for i in range(len(scores)):
    sum = 0
    avg = 0.0

    korTotal += scores[i][0]
    engTotal += scores[i][1]
    mathTotal += scores[i][2]

    print("%3d" % (i+1), end='\t')
    for j in range(len(scores[i])):
        sum += scores[i][j]
        print("\t%d" % scores[i][j], end='\t')

    allTotal += sum
    avg = sum / len(scores[i])
    allAvg += avg
    print("\t%d\t\t%.2f" % (sum, avg))
allAvg /= len(scores)
print('--------------------------')
print("총점\t\t%d\t\t%d\t\t%d\t\t%d\t\t%.2f" % (korTotal, engTotal, mathTotal, allTotal, allAvg))

