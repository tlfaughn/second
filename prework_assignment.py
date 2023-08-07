############################ QUESTION 1 ############################

# Write a function to print "hello_USERNAME!" USERNAME is the input 
# of the function. The first line of the code has been defined as below.


def hello_name(user_name):
    print("Hello, " + user_name)

hello_name('USERNAME')


############################ QUESTION 2 ############################

# Write a python function, first_odds that prints the odd numbers 
# from 1-100 and returns nothing


def first_odds(x):
    for x in range(1, 100):
        x + 2
        print(x, end=" ")
    
first_odds(1)


############################ QUESTION 3 ############################

# Please write a Python function, max_num_in_list to return the max 
# number of a given list. The first line of the code has been defined 
# as below.


def max_num_in_list(a_list):
    a_list = [4, 6, 2, 1, 34, 29, 85, 7, 10, 24, 80]
    print(max(a_list))

max_num_in_list(max)


############################ QUESTION 4 ############################

# Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400. The return should be boolean Type
# (true/false).


def is_leap_year(year):
    a_year = False

    if (year % 400 == 0) and (year % 100 == 0):
        a_year = True

    elif (year % 4 == 0) and (year % 100 != 0):
        a_year = True

    else:
        pass

    return a_year

print(is_leap_year(2015))
print(is_leap_year(2000))
print(is_leap_year(1900))

############################ QUESTION 5 ############################

# Write a function to check to see if all numbers in list are 
# consecutive numbers. For example, [2,3,4,5,6,7] are consecutive
# numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.


def is_consectuive(a_list):
   return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

nums_1 = [3, 5, 7, 9, 1, 2, 4, 6, 8]
nums_2 = [3, 6, 38, 75, 37, 2001, 2023]
print(is_consectuive(nums_1))
print(is_consectuive(nums_2))
