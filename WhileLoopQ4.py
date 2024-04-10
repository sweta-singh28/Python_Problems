#search an element
nums = (1,4,3,2,8,10,18,16,23,55)
#printing the element
x = 23
i = 0
while i<len(nums):
    if nums[i] == x:
        print("Found at inedex: ", i)
    
    i += 1