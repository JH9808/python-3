import re #导入
pattern = '\d\.\d +'  # +限定符， \d 0_9数字出现1次或多次
s = 'I study python 3.11 every day'  # 待匹配字符串
match = re.match(pattern, s, re.I)
print(match)  #None
print('-'*50)




print('匹配值的起始位置:', match.start())
print('匹配值的结束位置：', match.end())
print('匹配区间的位置元素：', match.span())
print('待匹配的字符串：', match.string)
print('匹配的数据：', match.group())
