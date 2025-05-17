# Date: 5/16/2025
# Description: Function that takes a list
#              and reverses it

def reverse_list(input_list):
    """Takes a list and reverses it."""
    # Put the outermost items of the list in reverse order and move
    # towards the center
    # Converting float to int will automatically floor the number,
    # which is what we want.
    for index in range(int(len(input_list) / 2)):
        # Assign variables to these values so that the first mutation
        # doesn't affect the second
        left_index = input_list[index]
        right_index = input_list[-index-1]
        input_list[index] = right_index
        input_list[-index-1] = left_index
    #If there is an odd input, the middle number does not need to be changed.
