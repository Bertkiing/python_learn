# Python中函数的参数可以设置默认值

def get_gender(sex='Unknown'):
    if sex is 'f':
        sex = "Female"
    elif sex is 'm':
        sex = "Male"
    print(sex)

get_gender('m')
get_gender('f')
get_gender()