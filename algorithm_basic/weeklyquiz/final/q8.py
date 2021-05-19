# Dummy 게임 (뱀게임)

def solution(N, K, L, apples, moves):
    result = 0
    board = list()
    for i in range(N+2):
        board.append([])
        for j in range(N+2):
            if i == 0 or i == N+1 or j == 0 or j == N+1:
                board[i].append(1)
            else:
                board[i].append(0)
            
            for apple in apples:
                if apple[0] == i and apple[1] ==j:
                    board[i][j] = 9
    
    moves_d = {}
    for i in moves:
        moves_d[i[0]] = i[1]
    
    c_dn = 120
    snake = [[1, 1], [1, 1]]
    result = 0 # 정답 : 시간

    while (True):
        result += 1
        # 이동전 머리 좌표 저장
        thead = snake[0]
        temp = snake[-1].copy()
        if len(snake) != 1:
            for i in range(len(snake)-1, 0, -1):
                snake[i] = snake[i-1].copy()
        # 방향값에 따른 머리 변화
        if c_dn % 4 == 0:
            snake[0][1] = snake[0][1] + 1
        elif c_dn % 4 == 1:
            snake[0][0] = snake[0][0] + 1
        elif c_dn % 4 == 2:
            snake[0][1] = snake[0][1] - 1
        elif c_dn % 4 == 3:
            snake[0][0] = snake[0][0] - 1
        
        
        x, y = snake[0]
        if board[x][y] == 9:
            snake.append(temp)
            board[x][y] = 0
        
        
        if board[x][y] == 1 or (len(snake) >2 and [x, y] in snake[1:]):
            break

        if result in moves_d:
            if moves_d[result] == 'D':
                c_dn += 1
            elif moves_d[result] =='L':
                c_dn -= 1

    return result


N = 6
K = 3
L = 3
apples = [(3, 4), (2, 5), (5, 3)]
moves = [(3, 'D'), (15, 'L'), (17, 'D')]
print(solution(N, K, L, apples, moves))
 
N = 10
K = 4
L = 4
apples = [(1, 2), (1, 3), (1, 4), (1, 5)]
moves = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
print(solution(N, K, L, apples, moves))
 
N = 10
K = 5
L = 4
apples = [(1, 5), (1, 3), (1, 2), (1, 6), (1, 7)]
moves = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
print(solution(N, K, L, apples, moves))
 

N = int(input())
K = int(input())
apples = list()
for i in range(K):
    apples.append(list(map(int, input().split())))

L = int(input())
moves = list()
for i in range(L):
    a, b = input().split()
    moves.append((int(a), b))

print(solution(N, K, L, apples, moves))