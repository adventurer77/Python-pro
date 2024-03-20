
# Task 1


def apply_sum(numbers, func1):
    return sum(func1(num) for num in numbers)

numbers = [1, 2, 3, 4, 5]
func1 = lambda x: x * 2
print(apply_sum(numbers, func1))


# Task 2

def save_res_to_file(func):
    """
    This is a decorator function that saves the result of the function it decorates to a file.

    Args:
        func (function): The function whose result is to be saved.

    Returns:
        wrapper (function): The decorated function with added functionality to save the result to a file.
    """

    def wrapper(*args, **kwargs):
        """
        This is the wrapper function that will be called instead of the original function.

        Args:
            *args: Variable length argument list of the decorated function.
            **kwargs: Arbitrary keyword arguments of the decorated function.

        Returns:
            str: A message indicating that the result has been saved to a file.
        """
        with open("result.txt", "a") as file:
            file.write(f"{func(*args, **kwargs)}\n")
            return "File save"
            
    return wrapper


@save_res_to_file
def return_add(a,b):
    """
    This function adds two numbers and returns the result as a string.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        str: A string representing the addition of the two numbers.
    """
    return f"{a} + {b} = {a + b}"

@save_res_to_file
def return_subtraction(a,b):
    """
    This function subtracts the second number from the first and returns the result as a string.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        str: A string representing the subtraction of the two numbers.
    """
    return f"{a} - {b} = {a - b}"


@save_res_to_file
def return_multiplication(a,b):
    """
    This function multiplies two numbers and returns the result as a string.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        str: A string representing the multiplication of the two numbers.
    """

    return f"{a} * {b} = {a * b}"

@save_res_to_file
def return_division(a,b):
    """
    This function divides the first number by the second and returns the result as a string.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        str: A string representing the division of the two numbers.
    """

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
     """
    This is a decorator function that measures the execution time of the function it decorates.

    Args:
        func (function): The function for which to measure the execution time.

    Returns:
        wrapper (function): The decorated function with added functionality to measure execution time.
    """
     def wrapper(*args, **kwargs):
        """
        This is the wrapper function that will be called instead of the original function.

        Args:
            *args: Variable length argument list of the decorated function.
            **kwargs: Arbitrary keyword arguments of the decorated function.

        Returns:
            result: The result of the decorated function.
        """

        start_time = time.time()
        result = func(*args, **kwargs)
        # execution_time = round(time.time() - start_time, 1)
        execution_time = f"{time.time() - start_time:.1f}"
        print(f'Function execution time {func.__name__}: {execution_time} s.')
        return result

     return wrapper
            

@measure_time
def some_function():
    """
    This is a sample function that sleeps for a total of 6 seconds to demonstrate the use of the measure_time decorator.
    """
    time.sleep(2)
    time.sleep(4)

some_function()


# Task 4

def limit_calls(max_calls:int):
    """
    This is a decorator function that limits the number of calls to the function it decorates.

    Args:
        max_calls (int): The maximum number of calls allowed for the decorated function.

    Returns:
        decorator (function): The decorator function.
    """
     
    def decorator(func):
        """
        This is the decorator function that adds functionality to limit the number of calls to the decorated function.

        Args:
            func (function): The function to be decorated.

        Returns:
            wrapper (function): The decorated function with added functionality to limit the number of calls.
        """
            
        def wrapper(*args, **kwargs):
            """
            This is the wrapper function that will be called instead of the original function.

            Args:
                *args: Variable length argument list of the decorated function.
                **kwargs: Arbitrary keyword arguments of the decorated function.

            Returns:
                result: The result of the decorated function if the number of calls is within the limit.
            """

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
    """
    This is a decorator function that caches the results of the function it decorates.

    Args:
        func (function): The function whose results are to be cached.

    Returns:
        wrapper (function): The decorated function with added functionality to cache results.
    """
    
    my_cache = {}
    
    def wrapper(*args, **kwargs):
        """
        This is the wrapper function that will be called instead of the original function.

        Args:
            *args: Variable length argument list of the decorated function.
            **kwargs: Arbitrary keyword arguments of the decorated function.

        Returns:
            result: The cached result of the decorated function if it exists, otherwise the result of the function call.
        """
        cashe_key = args +tuple(kwargs.items())
        if cashe_key not in my_cache:
            my_cache[cashe_key] = func(*args,**kwargs)
        
        return my_cache[cashe_key]
    return wrapper

@cache_results
def fibonacci(n):
    """
    This function calculates the nth Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to calculate.

    Returns:
        int: The Fibonacci number.
    """
    
    if n <= 1:
        return n
    else:
        
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(50))  
print(fibonacci(50))  

end_time = time.time()

print("Execution time: ", end_time - start_time)





