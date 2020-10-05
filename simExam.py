

def solution(answers):
    answer = []
    p1 = 0
    p2 = 0
    p3 = 0

    for i in range(len(answers)):
        print(i)
        if((i+1)%5 != 0 and answers[i]==(i+1)%5):
            p1 += 1
        elif((i+1)%5 == 0 and answers[i]==5):
            p1 += 1

        if(i%2 == 0 and answers[i]==2):
            p2 += 1
        elif(i%8 == 1 and answers[i]==1):
            p2 += 1
        elif(i%8 == 3 and answers[i]==3):
            p2 += 1
        elif(i%8 == 5 and answers[i]==4):
            p2 += 1
        elif(i%8 == 7 and answers[i]==5):
            p2 += 1

        if((i%10 == 0 or i%10 == 1) and answers[i]==3):
            p3 += 1
        elif((i%10 == 2 or i%10 == 3) and answers[i]==1):
            p3 += 1
        elif((i%10 == 4 or i%10 == 5) and answers[i]==2):
            p3 += 1
        elif((i%10 == 6 or i%10 == 7) and answers[i]==4):
            p3 += 1
        elif((i%10 == 8 or i%10 == 9) and answers[i]==5):
            p3 += 1
    print('p1:',p1)
    print('p2:',p2)
    print('p3:',p3)
    temp = {}
    temp[1]=p1
    temp[2]=p2
    temp[3]=p3
    print(temp)
    temp = sorted(temp.items())
    print(temp)

    answer = list(a for a,b in temp)
    return answer


print('answer:', solution([1,2,3,4,5]))
print('answer:', solution([1,3,2,4,2]))
