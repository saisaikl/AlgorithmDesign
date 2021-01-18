x = input().split()
N = int(x[0])
M = int(x[1])
w = input().split()
v = input().split()
for i in range(N):
    w[i] = int(w[i])
    v[i] = int(v[i])

def maxVal(i,C):        # index i, capacity C
    if i == N:
        return 0
    else:
        skip = maxVal(i+1,C)
        if w[i] <= C:   # w[i] does not exceed capacity
            take = v[i] + maxVal(i+1,C-w[i])
        else:
            take = -1
        return max(skip, take)

print(maxVal(0,M))

    
