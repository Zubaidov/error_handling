hours = list(map(int,input("hours = ").split()))
target = int(input("target = "))
total = 0
for i in hours:
    if i>=target:
        total = total+1

print(total)

