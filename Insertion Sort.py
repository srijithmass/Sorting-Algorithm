'''
Program to sort the elements in the list using the Insertion Sort algorithm.
Developed by: SRIJITH R
RegisterNumber: 21004191
'''
def insertion_sort(nums):
    # Write your code here to sort the elements in the list using Insertion sort algorithm
    for i in range(1,len(nums)):
        item=nums[i]
        j=i-1
        while j>=0 and nums[j]>item:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=item
    return nums
list_of_nums = eval(input())
# use the insertion sort function to get the sorted list
value=insertion_sort(list_of_nums)
# print the sorted list
print(value)
