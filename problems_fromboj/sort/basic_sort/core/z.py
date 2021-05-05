# Z
# 2^n x 2^n 의 사각형을 z모양으로 탐색

N, r, c = input().split()
N = int(N)
r = int(r)
c = int(c)

def solution(N, r, c, sum):
    
    if N == 0:
        print(sum)
        return
    a = 2**(N-1)
    b = 2**(2*N-2)
    if r < a:       # 1행
        if c < a:    # 1행 1열
            solution(N-1, r, c, sum + 0*b)
        else:           # 1행 2열
            solution(N-1, r, c-a, sum + 1*b)
    else:               # 2행
        if c < a:   # 2행 1열
            solution(N-1, r-a, c, sum + 2*b)
        else:           # 2행 2열
            solution(N-1, r-a, c-a, sum + 3*b)
    
a = solution (N, r, c, 0)