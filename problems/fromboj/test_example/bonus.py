n = int(input())
s = input()

bonus = 0
sum = 0
for i in range(len(s)):
    if s[i] =='O':
        sum += i+1 + bonus
        bonus += 1
    if s[i] == 'X':
        bonus = 0

print(sum)