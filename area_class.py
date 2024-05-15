class Area:

    # def __init__(self, l, b):
    #     self.l = l
    #     self.b = b

    def calculateRectangleArea(self, l, b):
        rectangleArea = l * b
        return rectangleArea

    def calculateSquareArea(self, l):
        squareArea = l * l
        return squareArea


shape = input("Enter shape: ")
shape_variable = shape.lower()

if shape_variable == "rectangle":
    l = int(input("Enter length of rectangle: "))
    b = int(input("Enter breadth of rectangle: "))
    rectangleObj = Area()
    rectangleObj.calculateRectangleArea(l, b)
    print("The area of rectangle is: " +
          str(rectangleObj.calculateRectangleArea(l, b)))

elif shape_variable == "square":
    l = int(input("Enter length of square: "))
    squareObj = Area()
    squareObj.calculateSquareArea(l)
    print("The area of square is: " + str(squareObj.calculateSquareArea(l)))
else:
    print("Enter valid shape!!")
