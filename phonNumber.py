from collections import Counter

def solution3(phone_book):
    answer = True
    for i in range(0,len(phone_book)):
        for j in phone_book[0:i]+phone_book[i+1:len(phone_book)]:
            strA=str(phone_book[i])
            strB=str(j)
            lenA=len(str(phone_book[i]))
            lenB=len(str(j))
            if(lenA <= lenB):
                if(strA==strB[:lenA]):
                    answer = False
            else:
                if(strA[:lenB]==strB):
                    answer = False
    return answer


def solution2(phone_book):
    answer = True
    phone_book.sort()
    lenPhoneBook = len(phone_book)
    for i in range(0,lenPhoneBook-1):
        strA=str(phone_book[i])
        lenA=len(str(phone_book[i]))
        for j in range(i+1,lenPhoneBook):
            strB=str(phone_book[j])
            lenB=len(strB)
            if(strA==strB[:lenA]):
                answer = False
    return answer

# print()
# print('answer:', solution2([119, 97674223, 1195524421]))
# print()
# print('answer:', solution2([123,456,789]))
# print()
# print('answer:', solution2([12,123,1235,567,88]))
# print()
# print('answer:', solution2([1235789,127,129,12356,567,88]))


def solution7(phoneBook):
    for i in range(len(phoneBook)):
        phoneBook[i]=str(phoneBook[i])
    phoneBook.sort()

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        p1=str(p1)
        p2=str(p2)
        if p2.startswith(p1):
            return False
    return True



def solution6(phone_book):
    for i in range(len(phone_book)):
        pivot = str(phone_book[i])
        lenPivot = len(pivot)
        for j in range(i+1, len(phone_book)):
            strJ = str(phone_book[j])
            lenJ = len(strJ)
            strlen = min(lenPivot, lenJ)
            if pivot[:strlen] == strJ[:strlen]:
                return False
    return True



def solution8(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    print(hash_map)
    for phone_number in phone_book:
        temp = ""
        phone_number = str(phone_number)
        for number in range(len(phone_number)):
            temp += phone_number[number]
            print('temp:',temp)
            print('temp in hash_map:',temp in hash_map)
            print('temp != phone_number:',temp != phone_number)

            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

import re
def solution9(phoneBook):

    for b in phoneBook:
        b = str(b)
        p = re.compile("^"+b)
        print('type(p):',type(p))
        for b2 in phoneBook:
            b2 = str(b2)
            if b != b2 and p.match(b2):
                return False
    return True



# from itertools import combinations as c
from itertools \
import combinations as c
def solution(phoneBook):
    answer = True
    # for i in range(len(phoneBook)):
    #     phoneBook[i] = str(phoneBook[i])
    sortedPB = sorted(phoneBook) #, key= len)
    for (a,b) in c( sortedPB,2):
        a = str(a)
        b = str(b)
        if a == b[:len(a)]:
            answer = False
    return answer


print('answer:', solution([119, 97674223, 1195524421]))
print()
print('answer:', solution([123,456,789]))
print()
print('answer:', solution([12,123,1235,567,88]))
print()
print('answer:', solution([1235789,127,129,12356,567,88,56]))
