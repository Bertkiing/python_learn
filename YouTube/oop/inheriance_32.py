class Car:
    color = 'black'

    def print_color(self):
        print("Black")


# 表示Audi 继承了 Car
class Audi(Car):
    def print_brand(self):
        print("Audi")

    def print_color(self):
        print("White Audi")


audi = Audi()
audi.print_brand()
audi.print_color()
