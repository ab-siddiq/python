N = int(input())
b = list(map(int, input().split()))


frequency = {}
removalCount = 0


for x in b:
    if x in frequency:
        frequency[x] += 1
    else:
        frequency[x] = 1  


for x, freq in frequency.items():
    if freq > x:
        removalCount += freq - x
    elif freq < x:
        removalCount += freq
print(removalCount)
