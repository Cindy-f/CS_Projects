"""
# File: spiral.py
# Description: This program generates a spiral based on the dimension(auto-
# -generated) on the first line. It then takes in the inputs(which are numbers
# inside the spiral), sum all numbers adjacent to the input numbers, and finally
# output the sums.
# Student Name: Zhou Fan
# Student UT EID: zf2949
# Partner Name: （Olivia） Liuxin Pan
# Partner UT EID: lp28525
# Course Name: CS 313E
# Unique Number: 50775
# Date Created: 01/22/24
# Date Last Modified: 01/23/2024
"""

# pull request
def create_spiral(num):
    """This function creates a spiral with a dimension magnitude of num.
    Input: n is an odd integer between 1 and 100
    Output: returns a 2-D list representing a spiral
    if n is even add one to n
    """
    if num % 2 == 0:
        size = num+1
    else:
        size = num

    # initializes the array with all '0's: （list comprehension)
    arr = [[0] * size for _ in range(size)]

    # find the middle grid with 1 in it:
    start = size//2
    row = start
    col = start
    arr[row][col] = 1
    pos = 2

    # replace the '0's with numbers going from 1 to size*size
    # (starts from number '1' then move outwards till it goes
    # through the whole spiral)
    for i in range(1,size):
        # if i is odd, then go right and down.
        if i % 2 !=0:
            # go right for i units:
            for _ in range(i):
                col += 1
                arr[row][col] = pos
                pos += 1
            # go down for i units:
            for _ in range(i):
                row += 1
                arr[row][col] = pos
                pos += 1
        # if i is even, then go left and up.
        else:
            # go left for i units:
            for _ in range(i):
                col -= 1
                arr[row][col] = pos
                pos += 1
            # go up for i units:
            for _ in range(i):
                row -= 1
                arr[row][col] = pos
                pos += 1

    # outlier: finally go right for (size-1) units to close the spiral.
    for i in range(size-1):
        col += 1
        arr[row][col] = pos
        pos += 1

    return arr

def sum_adjacent_numbers(spiral, num):
    """
    Input: spiral is a 2-D list and num is an integer
    Output: returns an integer that is the sum of the
    numbers adjacent to num in the spiral.
    note: if num is outside the range return 0
    """
    size = len(spiral)

    if num > size*size:
        return 0

    # locate where n is in the spiral, store the location index in row and col.

    for i in range(size):
        for j in range(size):
            if spiral[i][j]==num:
                row = i
                col = j

    # any grid inside: (not on the edge nor on the corner)
    if 1<=row<=size-2 and 1<=col<=size-2:
        total = spiral[row-1][col-1] + spiral[row-1][col] + spiral[row-1][col+1] \
                + spiral[row][col-1] + spiral[row][col+1] + spiral[row+1][col-1] \
                + spiral[row+1][col] + spiral[row+1][col+1]

    # the upper left corner:
    elif row==0 and col==0:
        total = spiral[0][1] + spiral[1][0] + spiral[1][1]

    # the upper right corner:
    elif row==0 and col==size-1:
        total = spiral[0][size-2] + spiral[1][size-2] + spiral[1][size-1]

    # the lower left corner:
    elif row==size-1 and col==0:
        total = spiral[size-2][0] + spiral[size-2][1] + spiral[size-1][1]

    # the lower right corner:
    elif row==size-1 and col==size-1:
        total = spiral[size-2][size-2] + spiral[size-2][size-1] + spiral[size-1][size-2]

    # the upper edge:
    elif row==0 and 1<=col<=size-2:
        total = spiral[row][col-1] + spiral[row][col+1] \
        + spiral[row+1][col-1] + spiral[row+1][col] + spiral[row+1][col+1]

    # the lower edge:
    elif row==size-1 and 1<=col<=size-2:
        total = spiral[row][col-1] + spiral[row][col+1] \
        + spiral[row-1][col-1] + spiral[row-1][col] + spiral[row-1][col+1]

    # the left edge:
    elif 1<=row<=size-2 and col==0:
        total = spiral[row-1][col] + spiral[row-1][col+1] + spiral[row][col+1] \
        + spiral[row+1][col] + spiral[row+1][col+1]

    # the right edge:
    elif 1<=row<=size-2 and col==size-1:
        total = spiral[row-1][col-1] + spiral[row-1][col] + spiral[row][col-1] \
        + spiral[row+1][col-1] + spiral[row+1][col]

    return total

def sum_sub_grid(grid, val):
    """
    Input: grid a 2-D list containing a spiral of numbers
           val is a number within the range of numbers in
           the grid
    Output:
    sum_sub_grid returns the sum of the numbers (including val)
    surrounding the parameter val in the grid
    if val is out of bounds, returns 0
    """
    return sum_adjacent_numbers(grid, val)

def main():
    """
    A Main Function to read the data from input,
    run the program and print to the standard output.
    """

    # read the dimension of the grid and value from input file
    dim = int(input())

    # test that dimension is odd
    if dim % 2 == 0:
        dim += 1

    # create a 2-D list representing the spiral
    mat = create_spiral(dim)

    while True:
        try:
            sum_val = int(input())

            # find sum of adjacent terms
            adj_sum = sum_sub_grid(mat, sum_val)

            # print the sum
            print(adj_sum)
        except EOFError:
            break

if __name__ == "__main__":
    main()
