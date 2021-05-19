# a = [1, 2, 3, 4, 5]
# b = list()
# b.append(a.pop(3))
# print(a)
# a.insert(3, b.pop())
# print(a)
print(type('O'))

def solution(n, k, cmd):
    n = ['O']*n
    memory = list()
    for i in cmd:
        if len(i) == 1:
            if i == 'C':
                n[k] = 'X'
                memory.append(k)
                temp = k
                if k+1 >= len(n):
                    for i in range(k-1, -1, -1):
                        if n[i] == 'O':
                            k = i
                            break
                else:
                    flag = False
                    for i in range(k+1, len(n)):
                        if n[i] == 'O':
                            k = i
                            flag = True
                            break
                    if flag == False:
                        for i in range(k-1, -1, -1):
                            if n[i]=='0':
                                k = i
                                break
            if i == 'Z':
                n[memory.pop()] = 'O'
        else:
            com, num = i.split()
            cnt = 0
            num = int(num)
            if com == 'U':
                while (True):
                    if n[k-1] =='O':
                        k = k-1
                        cnt += 1
                    elif n[k-1] == 'X':
                        k = k-1
                    if num == cnt:
                        break
            if com == 'D':
                while (True):
                    if n[k+1] =='O':
                        k = k+1
                        cnt += 1
                    elif n[k+1] == 'X':
                        k = k+1
                    if num == cnt:
                        break

    answer = ''.join(n)
    return answer


n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n,k,cmd))
result = "OOOOXOOO"

cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n, k, cmd))