def solution(ins):
    ins.sort(key=lambda x:x[0])
    print(ins)
    min, max = ins[0]
    ins.pop(0)
    returnlist= list()
    for i in ins:
        if max < i[0]: # 겹치지 않음
            returnlist.append([min, max])    
            min, max = i
        elif i[0] <= max and max < i[1]: # 교집합이 존재
            max = i[1]
        else: # 포함 
            continue
    returnlist.append([min,max])
    return returnlist

        


print(solution([[1,4],[4,5]]))

