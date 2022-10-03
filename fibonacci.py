def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

inp = input('Enter num: ')
inp = int(inp)
if inp<=0:
    print('the input wrong')
else:
    print('fibonacci : ')
for i in range(inp):
        print(fibonacci(i))