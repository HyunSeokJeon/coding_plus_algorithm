def gcd(a, b):
    if a<b:
        a, b=b,a
    if a%b==0:
        return b
    else:
        return gcd(b, a-b)

print(gcd(128, 12))

def gcdString(A, B):
    if len(A) == len(B):
        if A == B:
            return A
        else:
            return ""
    if len(A) < len(B):
        A, B = B, A
    return gcdString(B, A[len(B):])

    
print(gcdString('fast', 'campus'))
