from rectangle import Rectangle,Square,Circle

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(), square_2.get_area_square())

cir_1 = Circle(5)
cir_2 = Circle(2)

print(cir_1.get_area_circle(), cir_2.get_area_circle())

figures = [rect_1,rect_2,square_1,square_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())