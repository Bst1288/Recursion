def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:])+string[0]

inp = input('Enter input: ')
print('string is',inp)
print('reverse string is',reverse(inp))