#list
print('#list')
a = [70,80,90,100]
b = [64,32,[30,40,50]]
c = ['python', 'anaconda', 'bulidup']
print('a', a)
print('str(a)', str(a))
print('', a[2:])
print('', a[:3])
print('', b[-1:3])
print()

#Value Comparison
print('#value Comparison')
print('a==a[:2]+a[2:]:', a==a[:2]+a[2:])
print('c*3:', c*3)

#id
temp = c
print('id(c):', id(c))
print('id(temp):', id(temp))
print()

#Operation
print('#operation')
a = [70,80,90,100]
b = [64,32,[30,40,50]]
c = ['python', 'anaconda', 'bulidup']
a.insert(len(a),130)
print('', a)
print('', a.count(82))
a.append(12)
print('after a.append(12):', a)
print('a.pop():', a.pop())
print('after a.pop():', a)
a.insert(2,111)
print('a.insert(2,111):', a)
del a[3]
print('del a[3]:', a)
a.remove(80)
print('after a.remove(80):', a)
print('', a[::])
print('', a[::-1])
print('', a[:1]+a[1:4])
a = a[:2]
print('', a)
a = a*7
a = a[0:2]+b[2:4]
print('', a)
print('id(a), id(a[0]):', id(a), id(a[0]))
print('', a)
a[2:]=[]
a.append(220)
print('', a)
a.sort()
print('', a)
a.append(230)
a.reverse()
print('', a)
a.extend([123,142])
print('', a)
temp = a
temp.extend([23])
print('', a)
print('', temp.index(23))
