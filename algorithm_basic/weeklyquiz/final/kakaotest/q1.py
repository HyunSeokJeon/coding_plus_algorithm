# 영어가 섞여있는 단어를 숫자로 만들어라

def solution(s):
    answer = 0
    en = [['one', '1'], ['two', '2'],['three', '3'], ['four', '4'],['five', '5'],
         ['six', '6'],['seven', '7'], ['eight', '8'],['nine', '9'], ['zero', '0']]
    for i in en:
        if i[0] in s:
            s = s.replace(i[0], i[1])
    return int(s)

print(solution('one4seveneightoneoneone'))

a = 'one4seveneightoneoneone'