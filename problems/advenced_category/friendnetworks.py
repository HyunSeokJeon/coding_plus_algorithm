# testcase = int(input())

testcase = 1

for _ in range(testcase):
    F = int(input())
    edges = list()
    for __ in range(F):
        edges.append(input().split())
    
    print(edges)

    ## 일단 패스