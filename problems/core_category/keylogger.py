testcase = int(input())
for _ in range(testcase):
    passlow = input()

    passstack = list()
    cursorstack = list()

    for i in passlow:
        if i =='<':
            if len(passstack) != 0:
                cursorstack.append(passstack.pop())
            continue    
        elif i =='>':
            if len(cursorstack) != 0:
                passstack.append(cursorstack.pop())
            continue   
        elif i =='-':
            if len(passstack) != 0:
                passstack.pop()
            continue    
        passstack.append(i)
    while len(cursorstack) != 0:
        passstack.append(cursorstack.pop())
    print(''.join(passstack))
