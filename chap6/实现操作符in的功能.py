def get_find(s, lst):
    for item in lst:
        if s == item:
            return True
    return False

lst = ['hello', 'world', ' python']
s = input('请输入你要判断的字符串')
result = get_find(s, lst)
print('存在' if result else '不存在') ##if ...else 的简写,三元运算符  if result == True  利用到对象的布尔值