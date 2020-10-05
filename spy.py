from itertools import combinations
from collections import Counter

def solution(clothes):
    answer = len(clothes)
    cType = ''
    cCount = 0
    dictA = Counter({})
    for (c1, c2) in clothes:
        # (c1, c2) = tuple(cloth)
        dictA += Counter({c2})
        print('dictA.keys():',dictA.keys())
        if cType != '' and cType != c2:
            cType = c2
            cCount += 1
    print(dictA)


    print(list(dictA.values())[0])
    dictA = list(dictA.values())

    cnt = 1
    for i in range(len(dictA)):
        cnt *= dictA[i]+1
        print('cnt:',cnt)
    cnt -= 1
    answer = cnt

    return answer

def solution2(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter(a+'a' for (name, a) in clothes)
    # for a in clothes:
    #     print('for counter',Counter())
    # cnt = Counter(clothes)
    print('cnt:',cnt)
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer


def solution4(c):
    from collections import Counter
    from functools import reduce
    answer=0
    print(Counter(x[1] for x in c).values())
    print([a+1 for a in Counter(x[1] for x in c).values()])
    # answer=reduce(lambda x,y:x*y,[a+1 for a in Counter(x[1] for x in c).values()])-1
    answer=reduce(lambda x,y:x*(y+1),Counter(x[1] for x in c).values(),1)-1
    return answer


print("answer:",solution([['yellow_hat', 'headgear'], \
                        ['blue_sunglasses', 'eyewear'], \
                        ['green_turban', 'headgear']]))
print()
print("answer:",solution([['headgear', 'yellow_hat'], \
                        ['eyewear', 'blue_sunglasses'], \
                        ['headgear', 'green_turban']]))
print()
print("answer:",solution([['yellow_hat', 'headgear'], \
                        ['blue_sunglasses', 'eyewear'], \
                        ['crow_mask', 'face'], \
                        ['smoky_makeup', 'face'], \
                        ['green_turban', 'headgear']]))
print()
print("answer:",solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))

listA = [1,2,3,]
print('listA:', listA)
print('a+1:',[a+1 for a in listA])
