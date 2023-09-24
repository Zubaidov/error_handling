nums = [9,-5,-5,5,-5,-4,-6,6,-6]
target = 3
count = 0

for i in range(len(nums)):
    for j in range(len(nums)):
        if i<j and nums[i]+nums[j]<target:
            count+=1

print(count)