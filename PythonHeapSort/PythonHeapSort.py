import sys

def heapData(nums,index,heapSize):
    largestNum = index
    leftIndex = 2 * index + 1
    rightIndex = 2 * index + 2
    if(leftIndex < heapSize and nums[leftIndex] > nums[largestNum]):
        largestNum = leftIndex

    if(rightIndex < heapSize and nums[rightIndex] > nums[largestNum]):
        largestNum = rightIndex
    if(largestNum != index):
        nums[largestNum], nums[index] = nums[index], nums[largestNum]
        heapData(nums,largestNum,heapSize)

def heapSort(nums):
    n = len(nums)
    for i in range(n // 2 -1, -1, -1):
        heapData(nums,i,n)
    for i in range(n-1,0,-1):
        nums[0],nums[i] = nums[i], nums[0]
        heapData(nums,0,i)
    return nums

user_input = input("Input numbers separated by a comma:\n").strip()
nums = [int(item) for item in user_input.split(',')]
heapSort(nums)
print(nums)

def pancakeSort(nums):
    arrLen = len(nums)
    while(arrLen > 1):
        mi = nums.index(max(nums[0:arrLen]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arrLen-1::-1] + nums[arrLen:len(nums)]
        arrLen = arrLen - 1
    return nums

user_input2 = input("Input numbers separated by a comma for Pancake Sort:\n").strip()
nums2 = [int(item) for item in user_input2.split(',')]
print(pancakeSort(nums2))




















