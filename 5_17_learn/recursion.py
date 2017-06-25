def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])

def mysum_1(L):
    return 0 if not L else L[0] + mysum_1(L[1:])    # Use  ternary(三元的) expression

def mysum_2(L):
    return L[0] if len(L) == 1 else L[0] + mysum_2(L[1:])  # Any type , assume one

def mysum_3(L):
    first, *rest = L
    return first if not rest else first + mysum_3(rest)   # Use 3.0 ext seq assign(分配)

### 上面的都是直接调用

def mysum_indirect(L):
    if not L:return 0
    return nonempty(L);

#间接递归
def nonempty(L):
    return L[0]+ mysum_indirect(L[1:])

#Python 尽量不必使用递归；(递归在内存空间和执行效率方面效率较低)


#处理[1,[2,3,4],5,[6,7]]
def sumtree(L):
    tot = 0
    for x in L:
        #判断 x 是不是list
        if not isinstance(x,list):
            tot += x
        else:
            tot += sumtree(x)
    return tot