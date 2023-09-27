# logs = [[1993,1999],[2000,2010]]
logs = [[1950,1961],[1960,1971],[1970,1981]]
logs_list = list(map(lambda i: logs[i][1]-logs[i+1][0], range(len(logs)-1)))
all_data = []
if max(logs_list)==min(logs_list) and max(logs_list)>0:
    for i in range(len(logs)-1):
        all_data.append(max(logs[i]))

print(min(all_data)-1)