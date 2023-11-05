lst =[54, 56, 77, 4, 567, 34]
#排序操作
asc_lst = sorted(lst)  #升序
desc_lst = sorted(lst, reverse = True)  #降序
print('原列表', lst)
print('升序', asc_lst)
print('降序', desc_lst)

#reversed 反向
new_lst = reversed(lst)
print(type(new_lst))
print(list(new_lst))

#zip
x = ['a', 'b', 'c', 'd']
y = [10, 20, 30, 40, 50]
zipobj = zip(x, y)
print(type(zipobj))
#print(list(zipobj))

#enumerate
enum = enumerate(y, start=1)
print(type(enum))
print(tuple(enum))

#all
lst2 = [10, 20, '', 30]
print(all(lst2))
print(all(lst))

#any
print(any(lst2))

#next
print(next(zipobj))
print(next(zipobj))
print(next(zipobj))

def fun(num):
    return num%2 ==1

obj = filter(fun, range(10))
print(list(obj))
#
def upper(x):
    return x.upper()

new_lst2=['hello', 'world', 'python']
obj2=map(upper, new_lst2)
print(list(obj2))