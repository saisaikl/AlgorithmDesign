class obj:
    def __init__(self,w,v):
        self.w = w
        self.v = v
        self.r = v/w

x = input().split()
n = int(x[0])
M = int(x[1])
w = input().split()
v = input().split()
item = []
for i in range(n):
    item.append(obj(int(w[i]), int(v[i])))

def getKey(x):
    return x.r    

item.sort(key=getKey, reverse=True)
	
def Bound(i, C):	# object i -> n-1, capacity = C
    global item, n
    
    sw = 0
    sv = 0
    j = i
    f = 1.0
    while j < n and f == 1.0:
        wj = min(C-sw, item[j].w)
        f = float(wj)/item[j].w
        sw += f*item[j].w
        sv += f*item[j].v
        j += 1
    return sv

print(Bound(0,M))
