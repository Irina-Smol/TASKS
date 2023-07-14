# Write an algorithm that takes an array and moves all of the zeros to the end, preserving
# the order of the other elements

# EXAMPLE: move_zeros([1, 0, 1, 2, 0, 1, 3]) -> returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    return [i for i in lst if i != 0] + [0] * lst.count(0)
