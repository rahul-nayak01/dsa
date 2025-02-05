def my_p(arr):
    ans=0
    for i in range(len(arr)+1):
        ans=ans^i
    for num in arr:
        ans=ans^num
    return ans


print(my_p([1,3,0]))