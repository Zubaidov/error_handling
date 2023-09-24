#nums = list(map(int, input().split()))
nums = [3,1,2,10,1]
fin_nums = []
lambnums = 0
for i in nums:
    lambnums+=i
    fin_nums.append(lambnums)

print(fin_nums)