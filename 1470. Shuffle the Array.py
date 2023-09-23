mylist = list(map(int, input().split()))
new_list = []
n = int(input())

for i in range(n):
    print(f'{mylist[i]}, {mylist[n+i]}')
    new_list.append(mylist[i])
    new_list.append(mylist[n+i])

print(new_list)