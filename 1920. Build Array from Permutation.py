nums = list(map(int, input().split()))
new_nums = []

for i in range(0, len(nums)):
    print(i)
    new_nums.append(nums[nums[i]])

print(new_nums)