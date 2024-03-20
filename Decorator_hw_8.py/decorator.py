
# Task 1


def apply_sum(numbers, func1):
    return sum(func1(num) for num in numbers)

numbers = [1, 2, 3, 4, 5]
func1 = lambda x: x * 2
print(apply_sum(numbers, func1))


# Task 2

def save_res_to_file(func):
    def wrapper(*args, **kwargs):
        with open("result.txt", "a") as file:
            file.write(f"{func(*args, **kwargs)}\n")
            return "File save"
            
    return wrapper


@save_res_to_file
def return_add(a,b):
    return f"{a} + {b} = {a + b}"

@save_res_to_file
def return_subtraction(a,b):
    return f"{a} - {b} = {a - b}"


@save_res_to_file
def return_multiplication(a,b):
    return f"{a} * {b} = {a * b}"

@save_res_to_file
def return_division(a,b):
    return f"{a} / {b} = {a / b}"


a,b = int(input("Entre first number>> ")),int(input("Entre second number>> "))

if a or b < 0:
    print(return_add(a,b))
    print(return_subtraction(a,b))
    print(return_multiplication(a,b))
elif a or b == 0:
    print(return_add(a,b))
    print(return_subtraction(a,b))
else:
    print(return_add(a,b))
    print(return_subtraction(a,b))
    print(return_multiplication(a,b))
    print(return_division(a,b))



# Task 3

import time

def measure_time(func):
     
     def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        # execution_time = round(time.time() - start_time, 1)
        execution_time = f"{time.time() - start_time:.1f}"
        print(f'Function execution time {func.__name__}: {execution_time} s.')
        return result

     return wrapper
            

@measure_time
def some_function():
    time.sleep(2)
    time.sleep(4)

some_function()


# Task 4

def limit_calls(max_calls:int):
     
    def decorator(func):
            
        def wrapper(*args, **kwargs):

            wrapper.num_calls +=1 
            if wrapper.num_calls <= max_calls:
                
                print(f"Call {wrapper.num_calls} of {func.__name__}()")
                return func(*args, **kwargs)
            else:
                print("Stop calling functions!")
            
        wrapper.num_calls = 0   
        return wrapper
    return decorator

@limit_calls(3)
def some_function():
    print("Function call!")

some_function()
some_function()
some_function()
some_function()



# Task 5


import time

start_time = time.time()

def cache_results(func):
    
    my_cache = {}
    
    def wrapper(*args, **kwargs):
        cashe_key = args +tuple(kwargs.items())
        if cashe_key not in my_cache:
            my_cache[cashe_key] = func(*args,**kwargs)
        
        return my_cache[cashe_key]
    return wrapper

@cache_results
def fibonacci(n):
    
    if n <= 1:
        return n
    else:
        
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(100))  
print(fibonacci(100))  

end_time = time.time()

print("Execution time: ", end_time - start_time)





