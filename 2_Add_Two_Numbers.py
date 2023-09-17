def addTwoNumbers(l1, l2):
    l1 = l1[::-1]
    l2 = l2[::-1]
    mylists = [l1, l2]
    final = 0
    for mylist in mylists:
        mynumres = 0
        n = 1
        for i in mylist:
            mynum = (10**(len(mylist)-n)) * i
            mynumres+=mynum
            n+=1
        final += mynumres
    
    final_res = [int(dig) for dig in str(final)]
    
    return final_res[::-1]


l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

print(addTwoNumbers(l1, l2))