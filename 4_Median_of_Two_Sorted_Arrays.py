def findMedianSortedArrays(num1, num2):
    nums = num1+num2
    nums.sort()
    total = len(nums)-1
    if total%2==0:
        res = nums[int(total/2)]
    else:
        res = (nums[int(total/2)] + nums[int(total/2)+1])/2
    return res





arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
print(findMedianSortedArrays(arr1, arr2))