def factorial(num):
    if num == 0:
        return 1
    if num == 1:
        return num
    else:
        return num * factorial(num-1)

inp = int(input('Enter input: '))
if inp < 0:
    print('Wrong input.')
else:
    print('factorial is ',factorial(inp))