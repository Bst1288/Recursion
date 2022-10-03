def palindrome(list,n,i):
    if n==1:
        return True
    if list[i] == list[n-1]:
        return palindrome(list,n-1,i+1)
    else:
        return False

inp = input('Enter input: ')
if palindrome(inp,len(inp),0):
    print("'"+ inp +"' is palindrome")
else:
    print("'"+ inp +"' is not palindrome")