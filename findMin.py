def min(list):
    if len(list) == 1:
        return list[0]
    else:
        new = min(list[1:])
        return new if new<list[0] else list[0]

ls = list(map(int,input('Enter input: ').split()))
ans = min(ls)
print('Min is ',ans)