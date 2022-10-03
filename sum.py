def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

inp = int(input('Enter input: '))
print('sum is',sum(inp))
