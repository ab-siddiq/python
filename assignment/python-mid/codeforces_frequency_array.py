N, M = map(int, input().split())
A = list(map(int, input().split()))

freq = [0] * (M + 1)

for num in A:
    freq[num] += 1

for i in range(1, M + 1):
    print(freq[i])
