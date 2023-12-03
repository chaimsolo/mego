class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.area = 0
        self.perimeter = 0



    def areaf(self):
        area = self.width * self.height
        return area

    def perimeterf(self):
        perimeter = self.width * 2 + self.height * 2
        return perimeter

    def input(self):
        self.width = int(input("Enter the width >>> "))
        self.height = int(input("Enter the height >>> "))

    def print(self):
        self.input()
        print("The area of the rectangle is {:.2f}".format(self.areaf()))
        print("The perimeter of the rectangle is {:.2f}".format(self.perimeterf()))
        print(" *  " * self.width)
        for i in range(self.height):
            print("*" + "    " * self.width + "*")
        print(" *  " * self.width)



rec1 = Rectangle()

rec2 = Rectangle()
rec1.print2()
rec2.print2()



