# age = int(input("What' your fav number?\n"))
# print(age)

"""
很显然，Python中的异常处理关键字没有catch：
try , except , finally 
"""

while True:
    try:
        number = int(input("What is your fav number\n"))
        print(18 / number)
        break
    except ZeroDivisionError:
        print("division by zero")
    except ValueError:
        print("Make sure and enter a number")
    except:
        print("unknown error !!!")
        break
    finally:
        print("loop complete")
