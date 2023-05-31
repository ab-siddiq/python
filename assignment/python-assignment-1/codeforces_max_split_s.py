str = input()
i=0
lCount=0
rCount=0
count=0
start=0
result = []
while i < len(str):
    
    if str[i]=="L":
        lCount=lCount+1
    if str[i]=="R":
        rCount=rCount+1
    if(lCount==rCount):
        count=count+1
        result.append(str[start:i+1])
        start=start+rCount+lCount
        rCount=0
        lCount=0
    i=i+1
print(count)
for i in result:
    print(i)

