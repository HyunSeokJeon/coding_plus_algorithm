def printa(answer):
    returnstr = ''
    for n in answer:
        returnstr += (str(n) + ' ')
    return returnstr.strip()

print(len(printa([1, 2, 3, 4])))
print(printa([1, 2, 3, 4]))
