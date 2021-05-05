# K번째 수
import sys

n, k = sys.stdin.readline().split()
data = list(map(int, sys.stdin.readline().split()))
data.sort()
print(data[int(k)-1])