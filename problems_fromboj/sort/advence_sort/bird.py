# 새


n = int(input())
cnt = 0
while n != 0:
    for i in range(1, 1000000):
        if n < i*(i+1)//2:
            i -= 1
            n -= i*(i+1)//2
            cnt += i
            break
print(cnt)