def sort_012(input_list):
    
    """
    The idea is to put 0 and 2 in their correct positions, which will make sure
    all the 1s are automatically placed in their right positions
    """
    #return -1 if there is no element in the input_list
    if len(input_list) ==0:
        return -1

    # initialize pointers for next positions of 0 and 2
    next_pos_0 = 0
    next_pos_2 = len(input_list) - 1

    front_index = 0
    correct_input = {0, 1, 2}
    
    while front_index <= next_pos_2:
        #sorting all the possible 0s to the front of the input_list
        if input_list[front_index] == 0:
            input_list[front_index] = input_list[next_pos_0]
            input_list[next_pos_0] = 0
            next_pos_0 += 1
            front_index += 1

        #sorting all the possible 2s from end to begining in the input_list
        elif input_list[front_index] == 2:           
            input_list[front_index] = input_list[next_pos_2] 
            input_list[next_pos_2] = 2
            next_pos_2 -= 1
            
        #return -1 if found value(s) other than 0s, 1s, or 2s
        elif input_list[front_index] not in correct_input:
            print("Error, please only included 0s, 1s, or 2s")
            return -1
        
        #sorting all the rest possible 1s between 0s and 2s
        else:
            front_index += 1


def test_function(test_case):
    sort_012(test_case)
    print(test_case)
    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

#test 1
test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]) #should print pass

#test 2
test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])   #should print pass

#test 3
test_case = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])        #should print pass

#test 4
test_case = []
test_function ([]) #should print pass

#test 5
test_case = [2, 1, 0]
test_function ([2, 1, 0]) #should print pass

#test 6
test_case = [3, 1, 0]
test_function([3, 1, 0]) #should print Fail because 3 is invalid value
