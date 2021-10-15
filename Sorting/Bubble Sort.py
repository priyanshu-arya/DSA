
from typing import List
from ran_list import rlist

def BubbleSort(nums: List[int]):
    #count_swaps = 0

    for i in range(len(nums)):
        #print(f'i: {i}')
        swapped = True
        for j in range(len(nums)-i-1):
            #print(nums)
            if nums[j] > nums[j+1]:
                #print(f'Swapping {nums[j]} and {nums[j+1]}')  
                nums[j], nums[j+1] = nums[j+1], nums[j]
                #swapped = False
                #count_swaps += 1
                swapped = False
            #print(f'j: {j}')
        if swapped:
            break

    #print(f'Soretd List is {nums} with total Number of Swaps {count_swaps}')
    print(nums)

if __name__ == '__main__':
    nums = rlist()
    BubbleSort(nums)