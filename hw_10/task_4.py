from abc import ABC, abstractmethod

class Figure(ABC):

    @abstractmethod
    def area():
        raise NotImplementedError("No")

    @abstractmethod
    def perimeter():
        raise NotImplementedError("No")


class Circle(Figure):

    def __init__(self,r:int|float,p:float = 3.14):
        if not isinstance(r,int|float):
            raise TypeError("The radius of the circle must be a number.")
        if not isinstance(p, float):
            raise TypeError("Pi must be a number.")
        self.r = r
        self.p = p
        

    def area(self):
        return self.p * (self.r ** 2)

    def perimeter(self):
        return 2 * self.p * self.r

class Rectangle(Figure):

    def __init__(self,a:int ,b:int):
        if not isinstance(a,int|float):
            raise TypeError("The a must be a number.")
        if not isinstance(b,int|float):
            raise TypeError("The b must be a number.")
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b
        # print(self.a * self.b)

    def perimeter(self) :
        return (self.a*2) + (self.b*2)
    

class Triangle(Figure):

    def __init__(self,a:int ,b:int,c:int, h:int):
        if not isinstance(a,int|float):
            raise TypeError("The a must be a number.")
        if not isinstance(b,int|float):
            raise TypeError("The b must be a number.")
        if not isinstance(c,int|float):
            raise TypeError("The c must be a number.")
        if not isinstance(h,int|float):
            raise TypeError("Height must be a number.")
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def area(self):
        return (self.a *self.h)/2

    def perimeter(self):
        return self.a + self.b + self.c
    
if __name__ == "__main__":
    try:
        circle = Circle(5)
        print(f"Circle area: {circle.area()}")
        print(f"Circle perimeter: {circle.perimeter()}")

        rectangle = Rectangle(4, 3)
        print(f"Rectangle area: {rectangle.area()}")  
        print(f"Rectangle perimeter: {rectangle.perimeter()}")

        triangle = Triangle(3, 4, 5, 2)
        print(f"Triangle area: {triangle.area()}")
        print(f"Triangle perimeter: {triangle.perimeter()}")
        
    except TypeError as te:
        print(f"TypeError: {te}")
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        print("Done")