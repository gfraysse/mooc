K, M = map(int,raw_input().split())
N = []
L = []
for i in range(K):
    tmp = map(int,raw_input().split())
    N.append(tmp[0])
    L.append(tmp[1:])

#print K, M, N, L

total = 0
for i in range(len(N)):
    m = max(L[i])
    total += m * m

print total % 1000
