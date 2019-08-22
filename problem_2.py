def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    #Return -1 if the case input list is empty
    if len(input_list) == 0:
        return -1

    if len(input_list) == 1 and input_list[0] != number:
        return -1


    #initial the left index and right index
    left_index = 0
    right_index = len(input_list) - 1
    
    
    while left_index + 1 < right_index:
        mid_index = (left_index + right_index) //2
        mid_element = input_list[mid_index]

        

        # return the middle index if the number is equal to the middle element
        if mid_element == number:
            return mid_index

        

        # Condition 1: left_element < mid_element < right_element

        if input_list[left_index] < mid_element < input_list[right_index]:

            if number > mid_element:

                left_index = mid_index

            else:

                right_index = mid_index

        # Condition 2: middle_element > left_element and middle_element > right_element

        elif mid_element > input_list[left_index] and mid_element > input_list[right_index]:

            if input_list[left_index] <= number < mid_element:

                right_index = mid_index

            else:

                left_index = mid_index

        # Condition 3: middle_element < left_element and middle_element < right element

        elif mid_element < input_list[left_index] and mid_element < input_list[right_index]:

            if mid_element < number <= input_list[right_index]:

                left_index = mid_index

            else:

                right_index = mid_index
        

    if input_list[left_index] == number:

        return left_index
       
    elif input_list[right_index] == number:

        return right_index
    else:
        return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
             return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])  #should print pass as the index is 0
test_function([[6, 7, 8, 1, 2, 3, 4], 1])         #should print pass as the index is 3
test_function([[6, 7, 8, 1, 2, 3, 4], 10])        #should print pass as the index is -1
test_function([[],5])                             #should print pass as the index is -1.

test_function([[3], 5])                           #should print pass as 5 is not in the input_list.
test_function([[6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4], 2])  #should print pass as the index is 8.
