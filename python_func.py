
#无参无返回值
def printHi():
    print("Hello,world")
#单参无返回值
def  printName(name):
    print(name)

# 单参且有返回值
def add(a,b):
    return a + b
#测试用例
print(add(4,4))
print(add("Hello","world"))

def intersect(seq1,seq2):
    res = []
    for x in seq1:
        if(x in seq2):
            res.append(x)
    return res
#测试用例
print(intersect("SPAM","SCAM"))
print(intersect([1,2,3],[3,6]))

def intersect2(s1,s2):
    #列表解析表达式
    res = [x for x in s1 if x in s2]
    return res
print(intersect2("SPAM","SCAM"))
print(intersect2([1,2,3],[2,4]))

#很容易看出上面的函数是——多态的，
# 即:它可以支持多种类型，只要支持扩展对象接口