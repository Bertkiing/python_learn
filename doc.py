"""
Python的多行注释使用的是三重引号块字符串
"""

spam = 40
def square(x):
    """
    function documention
    can we have liver then ?
    """

    return x ** 2



print(square(4))
print(square.__doc__)
