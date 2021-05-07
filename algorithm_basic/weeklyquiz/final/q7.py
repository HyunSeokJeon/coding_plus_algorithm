# 나잡아봐라

# 코니는 처음 위치 C에서 1초 후 1만큼 움직이고, 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다.
# 즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.
# 브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
# 코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
# 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다.

def solution(C, B):
    count = {i:[] for i in range(0,634)}
    count[0].append(B)
    answer = 0
    for i in range(1, 634):
        Ci = C + int((i+1)*i/2)
        for j in count[i-1]:
            if not (j - 1 < 0):
                count[i].append(j-1)
            if not (j + 1 > 200000):
                count[i].append(j + 1)
            if not (j * 2 > 200000):
                count[i].append(j * 2)
        
        if Ci in count[i]:
            answer = i
            break


    return answer
 
print(solution(11, 2))

