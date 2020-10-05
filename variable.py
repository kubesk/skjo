
#Variable use
print('#Variable use')

#Assign
print('#assing')
n = 700
print('n =', n)
print()

#Assign at the same time
print('#Assign at the same time')
a = b = c = 700
print(a, b, c)
print('type(b):',type(b))
print()

#overwrite
print('#overwrite')
b = 'overwrite varable'
print('type(b):', type(b))
print('b =', b)
print()

#id
print('#id')
a=700
b=700
print('id(a):', id(a))
print('id(b):', id(b))
print('id(a) == id(b):', id(a) == id(b))
b+=1
print('id(b):', id(b))
print('id(a) == id(b):', id(a) == id(b))

#data type
varStr = 'python'
varStr2 = 'nice'
varInt = 8
varFloat = 10.0
varBool = True
varList = [varStr, varStr2]
varDict = {
    'name' : 'Python',
    'height' : 197
}

print('varStr:', varStr)
print('varStr2:', varStr2)
print('varInt:', varInt)
print('varFloat:', varFloat)
print('varBool:', varBool)
print('varList:', varList)
print('varDict:', varDict)

print('type(varStr):', type(varStr))
print('type(varStr2):', type(varStr2))
print('type(varInt):', type(varInt))
print('type(varFloat):', type(varFloat))
print('type(varBool):', type(varBool))
print('type(varList):', type(varList))
print('type(varDict):', type(varDict))
print()

#Operation
print('#Operation')
print('divmod(100,8)', divmod(100,8))
(x, y) = divmod(100,8)
print('(x, y):', (x, y))
print('100//8:', 100//8)
print('100%8:', 100%8)
print('pow(2,3):', pow(2,3), 2**3)

import math
print('pi:', math.pi)
print('ceil(pi):', math.floor(math.pi))
