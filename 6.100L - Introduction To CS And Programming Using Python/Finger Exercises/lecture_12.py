'''
    Implement the function that meets the specifications below:
'''


def count_sqrts(nums_list):
    """
    nums_list: a list
    Assumes that nums_list only contains positive numbers and that there are no duplicates.
    Returns how many elements in nums_list are exact squares of elements in the same list, including itself.
    """
    # Your code here
    quad_list = [quad for quad in nums_list if quad**2 in nums_list]
    return len(quad_list)


# Examples:    
print(count_sqrts([3, 4, 2, 1, 9, 25]))  # prints 3
