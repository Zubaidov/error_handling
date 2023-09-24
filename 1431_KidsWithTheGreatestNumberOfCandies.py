candies = list(map(int, input().split()))
extraCandies = int(input())

canextraCandies = list(map(lambda a: a+extraCandies, candies))


looplist = [i>=max(candies) for i in canextraCandies]

print(looplist)