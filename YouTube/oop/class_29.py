class Student:
    # Python中的构造函数__init__()

    def __init__(self, age):
        self.age = age

    def add_age(self):
        self.age += 1
        print(self.age)

    def is_adult(self):
        if self.age >= 18:
            print('You are a adult')
        else:
            print('You are young')


student1 = Student(16)
student1.add_age()
student1.is_adult()

student2 = Student(18)
student2.is_adult()
