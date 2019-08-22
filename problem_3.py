def mergesort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items

    # Otherwise, find the midpoint and split the list
    mid = len(items) // 2
    left = items[0:mid]
    right = items[mid:]

    # Call mergesort recursively with the left and right half
    left = mergesort(left)
    right = mergesort(right)

    # Merge our two halves and return
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0

    # Move through the lists until we have exhausted one
    while left_index < len(left) and right_index < len(right):

        # If right's item is larger, append right's item
        # and increment the index
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1

        # Otherwise, append left's item and increment
        else:
            merged.append(left[left_index])
            left_index += 1

    # Append any leftovers. Because we've broken from our while loop,
    # we know at least one is empty, and the remaining:
    # a) are already sorted
    # b) all sort past our last element in merged
    merged += left[left_index:]
    merged += right[right_index:]

    # return the ordered, merged list    
    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    #return -1 if the lenght of input list has none element or only one element
    if len(input_list) <= 1:
        return []



    #sorted the input list
    sorted_list = mergesort(input_list)

    #build two sum numbers
    first_num = sorted_list[0::2]
    second_num = sorted_list[1::2]

    
    
    first_num_string = ''
    for num in first_num:
        first_num_string += str(num)

    second_num_string = ''
    for num in second_num:
        second_num_string += str(num)

    

    

    return [int(first_num_string), int(second_num_string)]
    

    

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])   # should print pass       
test_function([[4, 6, 2, 5, 9, 8], [964, 852]]) # should print pass 
test_function([[2, 5], [5,2]]) #should print pass   
test_function([[],[]]) # should print pass
test_function([[1],[]]) # should print pass 
