# CIS40: Chapter 4 - Exercise 5: Nandhini Pandurangan
# This program calculates the sum of digits of an input number.


def calculate_num_sum():
    flag = True
    num = 0
    original = 0
    sum = 0

    # input validation
    while flag:
        try:
            num = int(input("Please enter an integer: "))
            original = num
            flag = False
        except:
            print("\n----- Please enter a valid integer ----\n")

    # evaluating the input
    if num == 0:
        sum = 0
    else:
        while num != 0:
            remainder = num % 10
            num = num // 10
            sum += remainder

    # outputting the results
    print("The sum of the digits of the integer {0} is {1}".format(original, sum))


# calling the function to solve the problem
calculate_num_sum()

'''
Please enter an integer: 123
The sum of the digits of the integer 123 is 6
--------------------------------------------------

Please enter an integer: hello

----- Please enter a valid integer ----

Please enter an integer: 22 23

----- Please enter a valid integer ----

Please enter an integer: 1234567890
The sum of the digits of the integer 1234567890 is 45
'''
