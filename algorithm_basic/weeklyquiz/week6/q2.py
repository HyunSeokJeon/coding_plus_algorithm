def solution(N, number):
    if N == number:
        return1
    numuset = [set() for _ in range(8)]
    answer = 0
    for i in range(8):
        numuset[i].add(int(str(N) * (i+1)))

    for numu in range(1, 8):
        for i in range(numu):
            for n1 in numuset[i]:
                for n2 in numuset[numu - i -1]:
                    numuset[numu].add(n1 + n2)
                    numuset[numu].add(n1 - n2)
                    numuset[numu].add(n1 * n2)
                    if n2 !=0:
                        numuset[numu].add(n1 / n2)
    for i in range(8):
        if number in numuset[i]:
            answer = i + 1
            break
    return answer



print(solution(2, 14))