class Spider:
    def show(self):
        print("spider")


class Person:
    def show_me(self):
        print('man')


# Python中的多继承
class SpiderMan(Spider, Person):
    def showing(self):
        print('SpiderMan')


spider_man = SpiderMan()
spider_man.show()
spider_man.show_me()
spider_man.showing()
