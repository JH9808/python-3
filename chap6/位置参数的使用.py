def happy_birthday(name, age):
    print('祝' + name + '生:快乐')
    print(str(age) + '岁生日快乐')

happy_birthday('娟子姐', 18)

happy_birthday('陈妹妹', age=18)  #位置传参，也可以使用关键字传参

#位置传参在前，关键字传参在后