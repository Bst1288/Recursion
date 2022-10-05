def Search(low,high,x):
    if(high<low):
        return -1
    mid = (low+high)//2
    if x == mid:
        return mid
    elif mid<x:
        return Search(mid+1,high,x)
    else: 
        return Search(low,mid-1,x)

ans = Search(0,8,17.5)
print(str(ans))