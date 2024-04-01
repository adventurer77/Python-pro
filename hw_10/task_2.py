class User:

    def __init__(self,first_name,second_name):

        self.__first_name = str(first_name).capitalize()
        self.__second_name = str(second_name).capitalize()
    

    @property
    def first_name(self):
       
       return self.__first_name
    
    @property
    def second_name(self):

        return self.__second_name
    
    def __setattr__(self,key,value):

        if key in ("first_name", "second_name"):
            raise AttributeError("You can't change it!")
        return object.__setattr__(self,key,value)
    
    def __getattr__(self,item):

        return f"Property '{item}' does not exist!"
    
if __name__ == "__main__":
    
    try:
        test = User("sam","fisher")
        print(f"First name: {test.first_name}")
        print(f"Secont name: {test.second_name}")

        test.first_name = "Bob"
        # test.second_name = "v" 
        

        # print(test.t)
            
    except Exception as e:
        print (e)
    finally:
        print("Done")

