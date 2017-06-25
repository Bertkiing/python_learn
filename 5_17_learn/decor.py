import sys


def decor(func):
    def wrap():
        print("================")
        func()
        print("===============")
    return wrap

def print_text():
    print("Hello,world")

# 加强版的print_text()
print_text1 = decor(print_text)

print_text()
print_text1();

print(sys.argv)