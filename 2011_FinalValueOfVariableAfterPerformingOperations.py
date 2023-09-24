operations = list(map(str, input().split()))
print(operations)

X=0

for i in operations:
    if i == '++X' or i == 'X++':
        X+=1
    elif i=='--X' or i == 'X--':
        X-=1

print(X)