#isdigit()十进制的阿拉伯数字
print('123'.isdigit())   #TRUE
print('一二三'.isdigit())  #FALSE
print('01bd23'.isdigit())  #FALSE

print('-'*50)
#所有字符都是数字
print('123'.isnumeric())  #TRUE
print('一二三'.isnumeric())  #TRUE
print('012gk324'.isnumeric())  #FALSE
print('壹贰'.isnumeric())   #TRUE
print('ⅠⅡⅢ'.isnumeric())  #TRUE

#所有字符都是字母（包含中文字符）
print('hello你好'.isalpha())  #TRUE
print('hello你好23435'.isalpha())   #FALSE
print('hello一二三'.isalpha())  #TRUE
print('helloⅠⅡⅢ'.isalpha())  #FALSE
#所有字符都是数字或字母
print('hello你好'.isalpha())  #TRUE
print('hello你好23435'.isalpha())   #TRUE
print('hello一二三'.isalpha())  #TRUE
print('helloⅠⅡⅢ'.isalpha())  #TRUE

#判断字符的大小写
print('Hello'.islower())  #FALSE
print('hello'.islower())  #TRUE
print('hello你好'.islower())  #TRUE

print('-'*50)
print('Hello'.isupper())  #FALSE
print('HELLO'.isupper())   #TRUE
print('HELLO你好'.isupper())   #TRUE
print('-'*50)
#所有字符都是首字母大写
print('Hello'.istitle())  #TRUE
print('HelloWorld'.istitle())  #FALSE
print('Helloworld'.title())  #TRUE
print('Hello World'.istitle())  #True
print('Hello world'.istitle())  #false
#判断是否都是空白符
print('\t'.isspace())  ##TRUE
print(' '.isspace())   #TRUE
print('\n'.isspace())  #TRUE