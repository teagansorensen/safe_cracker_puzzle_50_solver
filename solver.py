# imports
import numpy as np
from copy import deepcopy
import time

# setup puzzle
rings = np.array([
     [19,  0,  8,  0, 17,  0,  6,  0,  6,  0,  8,  0,  8,  0, 16,  0]
    ,[ 4, 14,  4,  5,  1, 14, 10, 17, 10,  5,  6, 18,  8, 17,  4, 20]
    ,[ 8,  0, 12,  0, 11,  0,  3,  0,  8,  0, 10,  0, 14,  0, 11,  0]
    ,[ 0,  5, 20,  8, 19, 10, 15, 20, 12, 20, 13, 13,  0, 22, 19, 10]
    ,[10,  0,  0,  0, 11,  0,  8,  0,  8,  0,  8,  0, 10,  0, 11,  0]
    ,[20, 12,  1, 10, 12, 22,  0,  5,  8,  5,  1, 24,  8, 10, 20,  7]
    ,[ 0,  9,  0,  8,  0,  8,  0,  9,  0,  6,  0, 10,  0,  8,  0, 10]
    ,[10, 10, 15,  7, 19, 18,  2,  9, 27, 13, 11, 13, 10, 18, 10, 10]
    ,[ 1, 10,  4,  5,  3, 15, 16,  4,  7,  0, 16,  8,  4, 15,  7, 10]
])
masks = np.array([
     [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ,[ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    ,[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ,[ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    ,[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ,[ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    ,[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ,[ 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    ,[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

# implement puzzle wheel rotation
def rotate_wheel_1(rings,masks):
    rings[0] = np.roll(rings[0], 1)
    masks[1] = np.roll(masks[1], 1)

def rotate_wheel_2(rings,masks):
    rings[1] = np.roll(rings[1], 1)
    rings[2] = np.roll(rings[2], 1)
    masks[3] = np.roll(masks[3], 1)

def rotate_wheel_3(rings,masks):
    rings[3] = np.roll(rings[3], 1)
    rings[4] = np.roll(rings[4], 1)
    masks[5] = np.roll(masks[5], 1)

def rotate_wheel_4(rings,masks):
    rings[5] = np.roll(rings[5], 1)
    rings[6] = np.roll(rings[6], 1)
    masks[7] = np.roll(masks[7], 1)

# implement solution check
def check_if_solution(rings_in,masks_in):

    # copy inputs
    rings = deepcopy(rings_in)
    masks = deepcopy(masks_in)

    # apply masks
    rings_masked = np.multiply(rings,masks)

    # get column sums
    column_sums = np.sum(rings_masked, axis=0)

    # if column sums are all 50, solution found
    if(list(column_sums) == [50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50] ): # #[47, 47, 38, 33, 60, 66, 34, 52, 55, 33, 52, 70, 45, 69, 54, 54]
        return(True)
    else:
        return(False)

# start cracking
print("cracking...")
start_time = time.time()
puzzle_cracked = False
for wheel_rotation_1 in range(16):
    if(not(puzzle_cracked)):
        rotate_wheel_1(rings,masks)
        puzzle_cracked = check_if_solution(rings,masks)
    for wheel_rotation_2 in range(16):
        if(not(puzzle_cracked)):
            rotate_wheel_2(rings,masks)
            puzzle_cracked = check_if_solution(rings,masks)
        for wheel_rotation_3 in range(16):
            if(not(puzzle_cracked)):
                rotate_wheel_3(rings,masks)
                puzzle_cracked = check_if_solution(rings,masks)
            for wheel_rotation_4 in range(16):
                if(not(puzzle_cracked)):
                    rotate_wheel_4(rings,masks)
                    puzzle_cracked = check_if_solution(rings,masks)


# output findings
if(puzzle_cracked):
    print("solution found!")
    print(f"time in seconds to find a solution: {np.round(time.time() - start_time,2)}")
    print("ring positions: ")
    print(rings)
    print("mask positions: ")
    print(masks)
else:
    print("no solution found")