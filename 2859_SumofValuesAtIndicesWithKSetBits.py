nums = [4,3,2,1]
k = 2
sumofnum=0
bin_nums = list(map(lambda i: bin(i).replace("0b", ""), range(len(nums))))
for j in bin_nums:
    if j.count('1')==k:
        sumofnum=sumofnum+nums[int(j, 2)]
print(sumofnum)
