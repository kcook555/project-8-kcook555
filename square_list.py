# Author: Kevin Phillips
# GitHub username: kcook555
# Date: 5/16/2025
# Description: Function that takes a list
#              of numbers and mutates it to
#              contain the squares of the original
#              numbers

def square_list(nums):
    """Takes a list of numbers and mutates the list to contain
    the squares of those numbers."""
    for index in range(len(nums)):
        nums[index] = nums[index]**2
