#Task 1

def counting_out(max_count:int, border:int ):
    """A generator function that finds the number of a geometric sequence of numbers.
    
    Args:
        max_count (int): The maximum value by which the counter will be multiplied.
        border (int): the bound of the counter, defines the number of numbers in the sequence.
    
    Yields:
        int: Returns one term of a geometric progression.
    """

    count = 1
    while count <= border:
             yield count * max_count
             count += 1


res = counting_out(int(input("Enter yot number>> ")),int(input("Enter yot border>> ")))
print(list(res))


#  Task 2

def my_range(my_number,border=0,step=0):
    """Generator function similar to the range function.
    
    Args:
        my_number (int): Start number of the range.
        border (int): Ending number of the range.
        step (int): Step number of the range.

    Yields:
        int: Returns numbers in a sequence within a given range. 
    """

    if step > 0:
        while  my_number <= border - 1:
            yield  my_number  
            my_number += step
    elif step < 0:
        while  border <= my_number - 1  :
            yield  my_number 
            my_number += step
    elif step == 0 and border != 0:
        while  my_number <= border - 1:
            yield  my_number 
            my_number += 1
    else:
        while  border <= my_number - 1  :
            yield  border
            border += 1


res = my_range(2,-14,-2)
print(list(res))



# Task 3

def prime_numbers(start, stop):
    """ Generator function for finding prime numbers in a given range.

    Args:
       start (int): coin number for the range.
       stop (int): Ending number of the range.

    Yields:
       int: A prime number in the given range.
    """
    
    for number in range(start, stop + 1):
        if number > 1:
            for i in range(2, int(number ** 0.5) + 1):
                if (number % i) == 0:
                    break
            else:
                yield number

for number in prime_numbers(1, 30):
    print(number)


#Task 4

print(list(pow(x,3) for x in range(2,(int(input("Enter border>> "))+ 1))))


# Task 5

def fibo(max_count):

    """Fibonacci number generator function.

    Args:
       max_count (int): The maximum number of numbers in the sequence.

    Yields:
       int: Returns the next number in the Fibonacci sequence at each iteration.
    
    """

    first, second = 0, 1
    for _ in range(max_count):
        yield second
        first, second = second, first + second

print(list(fibo(10)))


# Task 6

# import datetime

# def date_range(start_date, end_date):
    
#     for ordinal in range(start_date.toordinal(), end_date.toordinal()):
#         yield datetime.date.fromordinal(ordinal)


from datetime import datetime, timedelta

def generate_dates(start_date, end_date):
    """Generate a sequence of dates between a start date and an end date.

    Parameters:
    start_date (datetime): The start date of the sequence.
    end_date (datetime): The end date of the sequence.

    Yields:
    datetime: The next date in the sequence.
    """
    my_date = start_date
    while my_date <= end_date:
        yield my_date
        my_date += timedelta(days=1)

start = datetime(2023, 12, 1)
end   = datetime(2024, 1, 25)

# res = generate_dates(start_date,end_date)
print(list(generate_dates(start,end)))
