accounts = [[1,5],[7,3],[3,5]]
new_account = []
for i in range(len(accounts)):
    new_account.append(sum(accounts[i]))

print(max(new_account))