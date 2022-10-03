def power(num,p):
    if p == 0:
        return 1
    else:
        return num * power(num, p-1)

num,pow = input('Enter number and power : ').split()
num = int(num)
pow = int(pow)
ans = power(num,pow)
print('Power of',num,'by',pow,'is',ans)