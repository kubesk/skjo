

#Escape
print('#Escape')
print('null: \000')
print('I\'m a boy.')
print(bool(1))
print(bool(0))
print()

#Raw Str
print('#Raw Str')
print('c:\python-Basic\test')
print(r'c:\python-Basic\test')
print('ab'+'cd')
print()

#multi-line input
print('#multi-line input')
multiStr=\
'ab'+\
'cd'
print('multiStr:', multiStr)
print('type(multiStr):', type(multiStr))
print()

#basic Operation
print('#Operation')
str1 = 'Python'
str2 = 'anaconda'
str3 = '*'
print(str3*10)
print("'y' in str1:", 'y' in str1)
print("'Y' in str1:", 'Y' in str1)
print("'Y' not in str1:", 'Y' not in str1)
print('str1, str2:', str1, str2)
print('str1+str2:', str1+str2)
print(str3*10)
print()

#etc Operation
print('#etc Operation')
str1 = 'Python'
str2 = 'anaconda'
str3 = '*'
str4 = "good day gangs how are you"
print('str2.capitalize:', str2.capitalize())
print('str2.upper:', str2.upper())
print("str1.endswith('n'):", str1.endswith('n'))
print("str1.endswith('N'):", str1.endswith('N'))
print("str1.startswith('P'):", str1.startswith('P'))
print("str1.startswith('p'):", str1.startswith('p'))
print("str2.upper().startswith('A'):", str2.upper().startswith('A'))
print(str2+".replace('a','A'):", str2.replace('a','A'))
print(r'"'+str4+r'"'+".split(' '):", str4.split(' '))
# print(dir(str2))
print('for i in "{}":'.format(str2.upper()))
for i in str2.upper():
    print(i)
print('str2[2:4]:', str2[2:4])
print('str2[2:len(str2)]:', str2[2:len(str2)])
print('str2[2:]:', str2[2:])
print('str2[2:]:', str2[2:])
print('str2[2:]:', str2[2:])
print('str2[:-2]:', str2[:-2])
print('str2[1:-2]:', str2[1:-2])
print('str2[-4:]:', str2[-4:])
print('str2[-4::-1]:', str2[-4::-1])
print('', str1[::])
print('', str1[3::])
print('', str1[::-1])
print('', str1[4::-1])
print('', str1[-2::-1])
print()
