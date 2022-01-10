'''
Program to sort the elements in the list using the Selection Sort algorithm.
Developed by: SRIJITH R
RegisterNumber: 21004191
'''
def selection_sort(nums):
    # write your code here using selection sort
    for i in range(len(nums)):
        low_index=i
        for j in range(i+1,len(nums)):
            if (nums[j]<nums[low_index]):
                low_index=j
        nums[i],nums[low_index]=nums[low_index],nums[i]
    return nums
list_of_nums = eval(input())
# use the selection sort function
value=selection_sort(list_of_nums)
# print the sorted list
print(value)