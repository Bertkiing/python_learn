class Student:
    age = 17
    def addAge(self):
        self.age += 1
        print(self.age)

    def isAdult(self):
        if self.age >= 18:
            print('You are a adult')
        else:
            print('You are young')

student1 = Student()
student1.addAge()
student1.isAdult()

student2 = Student()
student2.isAdult()