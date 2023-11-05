import re
pattern = '黑客|破解|反扒'
s = '我想学习python,想破解一些'
new_s = re.sub(pattern, 'XXX', s)
print(new_s)


s2 = 'https://cn.bing.com/search?q=ysj&form=ANSPH1&refig=65438cc4f21b4c24bec69563700dcff4&pc=EDGEESS'
pattern2 = '[?|&]'
lst = re.split(pattern2, s2)
print(lst)