sentences = ["please wait", "continue to fight", "continue to win"]

nums = list(map(lambda i: len(i.split(" ")), sentences))

print(max(nums))