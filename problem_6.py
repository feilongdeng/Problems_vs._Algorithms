## Max and Min in a Unsorted Array

# In this problem, we will look for smallest and largest integer from a list of unsorted integers.
# The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    #return None if there is less or equal to one element in the given array
    if len(ints) <= 1:
        return None

    #initialize the minimun and maximum as the first element of the array
    smallest_num = ints[0]
    largest_num = ints[0]


    for num in ints:
        #find the smallest element 
        if num < smallest_num:
            smallest_num = num

        #find the largest element
        if num > largest_num:
            largest_num = num

    return smallest_num, largest_num
    
    

## Example Test Case of Ten Integers
import random

#test 1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")  #should print pass

#test 2
print("Pass" if ((None) == get_min_max([])) else "False") #should print pass

#test 3
print("Pass" if ((None) == get_min_max([1])) else "False") #should print pass


