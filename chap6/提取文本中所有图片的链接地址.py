import re
s = 'https://img1.baidu.com/it/u=23457678,3454657$fm=26&fmt=auto'
pattern = 'https://img\d{1}.baidu.com/it/u\d*,\d*$fm=26&fmt=auto'#模式字符串

lst = re.findall(pattern, s)
for item in lst:
    print(item)