#dictionary
print('# dictionary')
d1 = {'name':'skjo', 'age':18, 'locale':'kr'}
print('', d1['name'])
d2 = dict([
 ('name', 'eroo'),
 ('age', 28),
 ('locale', 'en')
])
d3 = dict(
    name='fly',
    age=38,
    locale='ge'
)
print('', d2['name'])
print('', d3['name'])
# print('', dir(d2))
print()

#items
print('# items')
composit = (d1, d2, d3)
print('', composit)
for i in composit :
    print(i, i.keys())
for i in composit :
    print('{}'.format(i), tuple(i.values()))
for i in composit :
    print('{}'.format(i), i.items())
d3['name']='popeyes'
print('d3:', d3)
