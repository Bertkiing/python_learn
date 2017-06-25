# 讨论一下变量作用域

a = 100

def corn():
    # a = 100
    print(a)

def fudge():
    print(a)

corn()
fudge()