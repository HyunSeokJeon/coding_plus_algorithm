# 완주 못한 선수

def solution(participant, completion):
    answer = ''
    i = 0
    participant.sort()
    completion.sort()
    while i < len(completion):
        if completion[i]!=participant[i]:
            answer = participant[i]
            break
        else:
            i+=1
        if answer == '':
            answer = participant[len(participant) - 1]
        
    return answer
 
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))
 
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))
 
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))