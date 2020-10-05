#Chapter 02-1
#Print
print('#print practice')
print('hello','python','world')
print('hello python world')
print()

#file
print('#file')
import sys
print('hello, world', file=sys.stdout)
print()

#Seperator
print('#Seperator Practice')
print('h', 'e', 'l', 'l', 'o', sep = '|', file=sys.stdout)
print()

#End
print('#End Practice')
print('Sweet home', end='~~~!')
print()
print()

#Format
print('#Format Practice')
print('Whats your favorite Scary Movie? %s? %s' % ('Scream','yes'))
print('Whats your favorite Scary Movie? {}? {}'.format('Scream','yes'))
print('Whats your favorite Scary Movie? {1}? {0}'.format('yes','Scream'))
print()

#%s
print('#%s spacing')
print('%s' % ('nice'))
print('%10s' % ('nice'))
print('%.3s' % ('nice'))
print('%10.3s' % ('nice'))
print()

print('#using format func')
print('{}'.format('nice'))
print('{0:10}'.format('nice'))
print('{:.3}'.format('nice'))
print('{:10.3}'.format('nice'))
print('{:>10.3}'.format('nice'))
print('{:<10.3}'.format('nice'))
print('{0:^10.3}'.format('nice'))
print()

#%d
print('#d spacing')
print('%d' % (153))
print('%2d' % (153))
print('%10d' % (153))
print()

print('#using Format func')
print('{}'.format(153))
print('{:2d}'.format(153))
print('{:10}'.format(153+2))
print('{:<10d}'.format(153))
print('{:^10d}'.format(153))
print()

#%f
print('#%f scaling')
print('%f' %(3.1415923648))
print('%1.3f' %(13.1415923648))
print('%2.3f' %(113.1415923648))
print('%2.1f' %(113.1415923648))
print('%4.5f' %(113.1415923648))
print('%10.3f' %(3.1415923648))
print('%010.3f' %(3.1415923648))
print('%10.9f' %(3.1415923648))
print('%010.9f' %(3.1415923648))
print()

print('#using format()')
print('{}'.format(3.1415923648))
print('{:1.4f}'.format(13.1415923648))
print('{:2.3f}'.format(113.1415923648))
print('{:2.1f}'.format(113.1415923648))
print('{:4.7}'.format(113.1415923648))
print('{:10.3}'.format(3.1415923648))
print('{:010.3f}'.format(3.1415923648))
print('{:10.9f}'.format(3.1415923648))
print('{:010.9f}'.format(3.1415923648))
