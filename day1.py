'''
Find the middle index mid.


Compare the middle element with the target value.


If equal, return the index.


If the target is smaller, repeat the search on the left subarray.


If the target is larger, repeat the search on the right subarray.


'''

list = [1, 3, 3, 3, 3, 4, 5, 5]
l, r = 0, len(list)-1


def binary(value):
    global list, l, r
    while l <= r:
        mid = (r-l+1)//2 + l
        if list[mid] == value:
            return mid
        elif list[mid] < value:
            l = mid + 1
        else:
            r = mid - 1

    return -1

'''
binary search variation to find the first occurence of target
'''


def binary2(value):
    global list, l, r
    while l <= r:
        mid = (r-l+1)//2 + l
        if list[mid] >= value:
            r = mid - 1
        elif list[mid] < value:
            l = mid + 1

    if list[l] == value:
        return l
    else:
        return -1

'''
binary search variation to find the last occurence of target
'''

def binary3(value):
    global list, l, r
    while l <= r:
        print(l, r)
        mid = (r-l+1)//2 + l
        if list[mid] <= value:
            l = mid+1
        else:
            r = mid - 1

    if list[l-1] == value:
        return l-1
    else:
        return -1

'''
 Index of least element greater than key 
'''

def binary4(list, value):
    l, r = 0, len(list)-1
    while l <= r:
        print(l, r)
        mid = (r-l+1)//2 + l
        if list[mid] <= value:
            l = mid+1
        else:
            r = mid - 1

    return l


'''
    Index of greatest element less than key
'''

def binary5(list, value):
    l, r = 0, len(list)-1
    while l <= r:
        mid = (r-l+1)//2 + l
        if list[mid] >= value:
            r = mid - 1
        elif list[mid] < value:
            l = mid + 1

    return l-1



def main():
    # nums = [1,2,3,3,3,3,3]
    # print(last_occurence(nums,2))
    run_tests2()
def run_tests():
  
    test_cases = [
        # target in middle, and greater element exists
        ([1, 3, 5, 7], 5, 3),
        
        # target matches last element
        ([1, 3, 5, 7], 7, 4),
        
        # target less than all elements
        ([10, 20, 30], 5, 0),

        # target greater than all elements
        ([1, 2, 3], 10, 3),

        # target between duplicates
        ([1, 2, 4, 4, 6], 4, 4),

        # duplicates: find strictly greater
        ([3, 3, 3, 4, 5], 3, 3),

        # all elements equal to target
        ([5, 5, 5], 5, 3),

        # empty list
        ([], 42, 0),

        # only one element and it's greater
        ([10], 5, 0),

        # only one element and it's not greater
        ([5], 5, 1),

        # multiple occurrences of greater element
        ([1, 2, 3, 6, 6, 6, 9], 4, 3),
    ]

    print("---least element greater than target test---")
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = binary4(nums, target)
        assert result == expected, f"Test {i} failed: expected {expected}, got {result}"
    print("All tests passed!")

def run_tests2():
  
    test_cases = [
        # target in middle, and smaller element exists
        ([1, 3, 5, 7], 5, 1),  # 3 is the greatest < 5
        
        # target matches first element
        ([1, 3, 5, 7], 1, -1),  # nothing less than 1

        # target greater than all
        ([10, 20, 30], 40, 2),  # 30 is greatest < 40

        # target less than all
        ([10, 20, 30], 5, -1),

        # duplicates: target in between duplicates
        ([1, 2, 4, 4, 6], 4, 1),  # 2 is the greatest < 4

        # all elements equal to target
        ([5, 5, 5], 5, -1),

        # all elements less than target
        ([1, 2, 3], 5, 2),

        # all elements greater than target
        ([6, 7, 8], 5, -1),

        # target between duplicates
        ([1, 1, 1, 2, 2, 3], 2, 2),

        # empty list
        ([], 42, -1),

        # only one element, and it's less
        ([3], 5, 0),

        # only one element, and it's not less
        ([5], 5, -1),
    ]

    print("---greatest element less than target test---")
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = binary5(nums, target)
        assert result == expected, f"Test {i} failed: expected {expected}, got {result}"
    print("All tests passed!")


if __name__ =='__main__':
    main()


