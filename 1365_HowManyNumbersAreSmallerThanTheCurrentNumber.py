nums = [8,1,2,2,3]
count=0
newlist = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]>nums[j]:
            count+=1
    newlist.append(count)
    count=0


print(newlist)