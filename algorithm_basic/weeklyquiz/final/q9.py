# 수식 최대화
import itertools

def solution(expression):
    cal = list()
    mark = list(itertools.permutations(['*', '-', '+'], 3))

    def calculate(expression, m, index):
        print(expression, m, index)
        if index == 3:
            return str(eval(expression))

        sym = m[index]
        splist = expression.split(sym)
        print(splist)
        for i in range(len(splist)):
            print(i)
            splist[i] = calculate(splist[i], m, index+1)
        
        cand = sym.join(splist)

        return str(eval(cand))
            
    for m in mark:
        a = int(calculate(expression, m, 0))
        if a < 0:
            a = -a
        cal.append(a)
    return max(cal)



    

 
# print(solution("100-200*300-500+20"))
# print(solution("50*6-3*2"))

print(solution("177-661*999*99-133+221+334+555-166-144-551-166*166-166*166-133*88*55-11*4+55*888*454*12+11-66+444*99"))

a = "177-661*999*99-133+221+334+555-166-144-551-166*166-166*166-133*88*55-11*4+55*888*454*12+11-66+444*99"
print(a.split('*'))