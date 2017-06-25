magicNumber = 26

'''
Python的注释：
单行用 # ;
多行用 6个单引号\'''注释内容\'''
'''

# ok this program find a magic number

print("Bert" + "king")

# print("hello " + 5)  Can't convert 'int' object to str implicitly

print(5,"Bertking")

for n in range(101):
    if n is magicNumber:
        # continue 跳过本次继续执行
        print(n,"is the magic number!")
        break  # 立刻结束循环
    else:
        print(n)
