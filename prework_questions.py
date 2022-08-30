# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input
# of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    """Display geeting to a user, the user_name appears in caps."""
    print("Hello_" + user_name.upper() +"!")

hello_name('username')



# Question 2
#  Write a python function, first_odds that prints the odd numbers 
# from 1-100 and returns nothing.

def first_odds():
    """Display only odd numbers from 1-100 and returns nothing"""
    for i in range(1,101,2):
        print(i)

#first_odds()



# Question 3

# Please write a Python function, max_num_in_list to return the
# max number of a given list.

def max_num_in_list(a_list):
    """Returns the max number of a given list"""
    return max(a_list)



# Question 4

# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """
        Return Boolean value if a leap year is divisible by 4, 
        but not divisible by 100, unless it is also divisible by 400. 
    """
    leap_year = True

    while leap_year == True:
        if a_year % 4 == 0 and (a_year % 100 != 0):
            leap_year = True
        elif a_year % 4 == 0 and (a_year % 100 == 0) and (a_year % 400 == 0):
                leap_year = True
        else:
            leap_year = False
        return leap_year


# Question 5
# Write a function to check to see if all numbers in list are consecutive 
# numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but 
# [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    """
        Return Boolean value, if all numbers in a list are consecutive
        numbers
    """
    return sorted(a_list) == list(range(a_list[0],a_list[-1]+1,+1))