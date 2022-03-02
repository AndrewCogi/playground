#define makeDict function
def makeDict(K,V):
    s=len(K) # same as len(V)
    D=dict()
    for i in range(s):
        D[K[i]]=V[i]
    return D

K=('4','5','6')
V=(1,2,3)
print(makeDict(K,V))
