def max(list):
    if len(list) == 1:
        return list[0]
    else:
        num = max(list[1:])
        return num if num>list[0] else list[0]

list = list(map(int,input('find max : ').split(' ')))
ans = max(list)
print('max : ',ans)