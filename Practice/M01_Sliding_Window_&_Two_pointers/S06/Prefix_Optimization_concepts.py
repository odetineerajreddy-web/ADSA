nums=[1,2,3,4]
n= len(nums)
res=[0]*n
for i in range(n):
    s=0
    for j in range(0,i+1):
        s+=nums[j]
    res[i]=s
print(res)