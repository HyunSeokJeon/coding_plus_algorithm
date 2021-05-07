# dummy 게임

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
    start = [1, 1]
    print(board)
    return result

N = 6
K = 3
L = 3
apples = [(3, 4), (2, 5), (5, 3)]
moves = [(3, 'D'), (15, 'L'), (17, 'D')]

solution(N, K, L, apples, moves)