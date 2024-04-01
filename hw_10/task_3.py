

class Rectangle:

    def __init__(self,width:int,height:int):
        if not isinstance(width,int|float):
            raise TypeError("The width must be a number.")
        if not isinstance(height,int|float):
            raise TypeError("The height must be a number.")
        if width <= 0:
            raise ValueError("Width must be positive.")
        if height <= 0:
            raise ValueError("Height must be positive.")
        
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    def __setattr__(self,key,value):

        if key in ("width", "height"):
            raise AttributeError("You can't change it!")
        return object.__setattr__(self,key,value)
    
    def _getattr__(self,item):
        
         return f"Property '{item}' does not exist!"
    
    def area(self):
        return self.__width * self.__height


if __name__ == "__main__":
    
    try:
        test = Rectangle(4, 3)
        print(f"Rectangle area: {test.area()}") 

        print(f"Width: {test.width}")
        print(f"Height: {test.height}")

        # test.width = 66
        test.height = 45 
        
        # print(test.t)
            
    except Exception as e:
        print (e)
    finally:
        print("Done")