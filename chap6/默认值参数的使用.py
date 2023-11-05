happy_birthday()
happy_birthday('陈妹妹') #位置传参
happy_birthday(age=13)  #关键字传参，name采用默认值


def fun(a, b=20):   ##a作为位置参数，b默认值参数
    pass


def fun(a=30, b):  #报错，当位置参数和默认值参数同时存在的时候，位置参数在后会被报错
    pass