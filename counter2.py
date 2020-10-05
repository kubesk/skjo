from collections import Counter

def solution(participant, completion):
    answer = list((Counter(participant) - Counter(completion)).keys())
    print((Counter(participant) - Counter(completion)).elements())
    print(answer)
    return answer.pop()


print('answer:', solution(['leo', 'kiki', 'eden'],['eden', 'kiki']))
print()

dictA = ('a', 'b', 'c', 'a')
print(Counter(dictA))
temp=('a',)
print(Counter(temp))
dictA = Counter(dictA) - Counter(temp)
print(dictA)
