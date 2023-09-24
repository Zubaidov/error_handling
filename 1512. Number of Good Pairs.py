from math import factorial as fact

nums = list(map(int, input().split()))
set_nums = set(nums)
total_combinations = 0

for x in set(nums):
    tp = nums.count(x)
    if tp>=2:
        n = int(fact(tp)/(fact(tp-2)*fact(2)))
        total_combinations+=n

print(total_combinations)