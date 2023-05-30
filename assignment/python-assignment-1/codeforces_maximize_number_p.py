
result=0
N = int(input())
A = list(map(int, input().split()))


def divideByTwo():
    i=0
    while i < len(A):
        A[i]=A[i]/2
        i=i+1
    checkEven()
def checkEven():
    
    i=0
    t=0
    while i < len(A):
        if A[i]%2==0:
            t=t+1
        else:
            break
        if t==len(A):
            global result
            result=result+1
            divideByTwo()
        i=i+1
    return result
print(checkEven())

