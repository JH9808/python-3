def calc(a, b):
    return a+b

print(calc(10, 20))

##匿名函数
s = lambda a, b:a+b  #s 表示就是一个匿名函数
print(type(s))  #function
#调用匿名函数
print(s(10, 20))
print('-'*30)
#列表的正常取值操作
lst = [10, 20, 30, 40, 50]
for i in range(len(lst)):
    print(lst[i])
print()

print('-'*30)
for i in range(len(lst)):
    result = lambda x:x[i]  #根据索引取值，rssult是类型function,x是形式参数
    print(result(lst))  #lst是实际参数

student_scores = [
    {'name':'陈梅梅','score':98},
    {'name':'王一一','score':95},
    {'name':'张天乐','score':100},
    {'name':'白雪儿','score':65},
]
#列表进行排序,排序的规则是字典只得成绩
student_scores.sort(key=lambda x:x.get('score'),reverse=True)
print(student_scores)