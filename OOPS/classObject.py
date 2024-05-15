class Area:
    # def __init__(self,l,b):
    #     self.l = l
    #     self.b = b

    def areaOfRectangle(self, l, b):
        area_of_rectangle = l*b
        return area_of_rectangle

    def areaOfSquare(self, l):
        area_of_square = l*l
        return area_of_square


areaOfShapesObj = Area()
rectangle_area = areaOfShapesObj.areaOfRectangle(66, 6)
print(f"The area of rectangle is {rectangle_area}.")
square_area = areaOfShapesObj.areaOfSquare
