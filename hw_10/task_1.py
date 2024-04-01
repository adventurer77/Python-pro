class Score:
    def __init__(self,balance):

        self.__balance = balance
    
    @property
    def balance(self):

        return self.__balance
    
    def __setattr__(self,key, value):

        if key == "balance":
            raise AttributeError("You can't change it!")
        return object.__setattr__(self,key,value)
        
    def __getattr__(self,item):

        return f"Property '{item}' does not exist!"


if __name__ == "__main__":

    try:
        test = Score(23)
        print(f"Balance: {test.balance}")
        # test.balance = 1
        print(test.t)
    except Exception as e:
        print(e)
    finally:
        print("Done")

