lst = [
    {}
]
name = input('请输入你要查询的演员')
for item in lst:
    print(item)  #字典
    actors_lst = item.get('actors')
    if name in actors_lst:
        title = item.get('title')
        print(title)
        print(name, '出演', title, '电影')
