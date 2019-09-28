#Emily Jetton
#COSC 450
# Python code to create a random array and implement quicksort

from random import seed
from random import randint

def helper(nums_list, low, high):
    pivot = nums_list[high]             #getting pivot number
    i = (low-1)                         #getting smaller boundary           

    for j in range(low,high):
        if nums_list[j] <= pivot:       #if the number at the current spot is less than or equal to pivot, swap
            i = i+1                     #increment index of smaller number
            nums_list[i],nums_list[j] = nums_list[j], nums_list[i]

    nums_list[i+1], nums_list[high] = nums_list[high],nums_list[i+1]
    return(i+1)


def quicksort(nums_list,low, high):
    if low < high:
        help = helper(nums_list, low, high)
        quicksort(nums_list, low, help-1)
        quicksort(nums_list, help+1, high)



nums_list = []
for _ in range(100):
    value = randint(0,100)
    nums_list.append(value)

print()
print("This is the original array:")
print(nums_list)

print()
low = 0
high = len(nums_list)
quicksort(nums_list, low, high-1 )
print("The sorted array is: ")
print(nums_list)

