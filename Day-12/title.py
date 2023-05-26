
#title: find largest sum subtuple 


def find_largest_sum_subtuple(tup):
    max_sum = float('-inf')
    largest_subtuple = ()

    # Iterate over all possible subtuple lengths
    for length in range(1, len(tup) + 1):
        # Iterate over all possible starting indices
        for start in range(len(tup) - length + 1):
            # Get the subtuple from the start index to start + length
            subtuple = tup[start:start + length]
            # Calculate the sum of the subtuple
            subtuple_sum = sum(subtuple)
            
            # Update the maximum sum and largest subtuple if a larger sum is found
            if subtuple_sum > max_sum:
                max_sum = subtuple_sum
                largest_subtuple = subtuple

    return largest_subtuple

# Example:
my_tuple = (1, -2, 3, 4, -5, 2)
largest_subtuple = find_largest_sum_subtuple(my_tuple)
print(largest_subtuple)
