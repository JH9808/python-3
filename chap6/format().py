print(format(3.14, '20'))  #数值型默认右对齐
print(format('hello', '20'))  #字符串默认左对齐
print(format('hello', '*<15'))  #<左对齐,*表示的填充符, 15表示的是显示宽度
print(format('hello', '*>20'))
print(format('hello', '*^20'))

print(format(3.2445, '.2f'))
print(format(20, 'b'))
print(format(20, 'o'))
print(format(20, 'x'))
print(format(20, 'X'))

print('-'*40)
print(len('helloworld'))
print(len([10, 20, 30, 40]))

print('-'*40)
print(id(10))
print(id('helloworld'))
print(type('hello'), type(10))

print(eval('10+30'))