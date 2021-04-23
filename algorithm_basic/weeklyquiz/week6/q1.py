# 순열 가지수

n = 3
nlist = list(range(1,n+1))
print(nlist)
f = list()

def aaa(nlist, index, endindex, f):
    
    if index == endindex:
        print(nlist)
        return nlist
    else:
        for n in range(index, len(nlist)):
            nlist[n], nlist[index] = nlist[index], nlist[n]
            
            aaa(nlist, index+1, endindex, f)
            
            nlist[n], nlist[index] = nlist[index], nlist[n]
print() 
print()
e = list()
e.append(aaa(nlist, 0, len(nlist)-1, f))
print(f)
print(e)
