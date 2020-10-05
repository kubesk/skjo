from collections import Counter

def solution1(n, lost, reserve):
    lost = list(Counter(lost) - Counter(reserve))
    reserve = list(Counter(reserve) - Counter(lost))

    for i in range(0,len(lost)):
        for j in range(0,len(reserve)):
            if (lost[i]==reserve[j] or lost[i]-1==reserve[j] or lost[i]+1==reserve[j]):
                lost[i]=-1
                reserve[j]=-1

    lost=list(Counter(lost))
    lost.remove(-1)

    reserve=list(Counter(reserve))
    reserve.remove(-1)

    answer = n - len(lost)
    print(lost)
    print(reserve)
    return answer



answer = list((Counter(participant) - Counter(completion)).elements())
print((Counter(participant) - Counter(completion)).elements())

# or lost[i]-1==reserve[j] or lost[i]+1==reserve[j]
# print('answer:', solution(5, [2, 4], [1, 3, 5]))
# print()
# print('answer:', solution(5, [2, 4], [3]))
