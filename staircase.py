def staircasePos(n,step):
    if step <= n :
        print("_"*(n-step),"#"*step,sep="")
        staircasePos(n,step+1)

def staircaseNeg(n,step):
    if step > 0 :
        print("_"*(n-step),"#"*step,sep="")
        staircaseNeg(n,step-1)

n = int(input("Enter Input : "))

if n == 0 :
    print("Not Draw!")
elif n > 0 :
    staircasePos(n,1)
else :
    n = abs(n)
    staircaseNeg(n,n)