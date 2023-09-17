try:
    mynum = int(input("Enter a number: "))
    if mynum == 5:
        print('Hello My friend')
    else:
        print('Hello Chuchi Kulobi')
except ValueError:
    print('You input the wrong format')