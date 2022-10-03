def gcd(num1,num2):
    num1 = abs(num1)
    num2 = abs(num2)
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    if num1 == num2:
        return num2
    if num1>num2:
        return gcd(num1-num2,num2)
    return gcd(num1,num2-num1)

num1,num2 = map(int,input('Enter num: ').split(' '))
print(num1,' and ',num2)
ans = gcd(num1,num2)
if(ans>=0):
    print('GCD is ',ans)
else:
    print('can,t find GCD.')