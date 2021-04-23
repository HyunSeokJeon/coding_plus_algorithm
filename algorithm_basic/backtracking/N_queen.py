# N_Queen 문제
# NxN 체스판에 퀸을 서로 잡을 수 없는 형태로 배치

def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True




def dfs(N, current_row, current_candidate, final_result):
    if current_row == N:
        final_result.append(current_candidate[:])
        return
    
    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            dfs(N, current_row+1, current_candidate, final_result)
            current_candidate.pop()


def n_queen(N):
    final_result = []
    dfs(N, 0, [], final_result)
    return final_result

print(n_queen(5))

# 무조건 혼자서 풀때까지
