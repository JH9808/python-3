age = input('请输入你的年龄：')

if age > '18':
    print('成年了！')

#
i= 1
while i < 10:
    print(i)
    i += 1

    ##
for i in range(3):
    uname = input('请输入用户名：')
    pwd = input('请输入密码：')
    if uname == 'admin' and pwd == 'admin':
        print('登入成功')
        break
    else:
        print('输入有误')
else:
    print('对不起，三次均输入错误')

#
lst = [11, 22, 33, 44]
print(lst[3])
lst = []
lst.append('A')
lst.append('B')
lst.append('C')
print(lst)