def sqrt(number, initial_guess=10):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if (number is None or number < 0):
        return None

    current_guess = initial_guess


    lower_bound = 0  # Lowest real value possible

    upper_bound = initial_guess  # Use initial guess as the original upper bound for the guess range



    # Shift the bounds of the guess range based on the (upper bound)^2 relative to the input number

    while upper_bound * upper_bound < number:

        lower_bound = upper_bound

        upper_bound = upper_bound * 2



    # If you got the guess right on the first try

    if upper_bound * upper_bound == number:

        return initial_guess



    # Otherwise we need to iterate between the lower and the upper bound

    while abs(current_guess - (upper_bound + lower_bound)//2) > 0:

        # Find the middle of the range

        midpoint = (upper_bound + lower_bound)//2



        # Return midpoint

        if midpoint * midpoint == number:

            return midpoint



        # Otherwise adjust the range appropriately based on the value of (midpoint)^2 relative to the bounds

        elif midpoint * midpoint > number:

            upper_bound = midpoint

        else:

            lower_bound = midpoint



        current_guess = midpoint



    return current_guess

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

print ("Pass" if ( 2 == sqrt(5)) else "Fail")
print ("Pass" if ( 2 == sqrt(8)) else "Fail")
print ("Pass" if ( None == sqrt(None)) else "Fail")

print(sqrt(-1))
print(sqrt(None))
print(sqrt(5))
