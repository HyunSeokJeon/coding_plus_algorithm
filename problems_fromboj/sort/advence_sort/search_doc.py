# 문서검색

rowstr = input()
target = input()

# rowstr = 'a a a a a'
# target = 'a a'

tlen = len(target)
cnt = 0
while True:
    if len(rowstr) < len(target):
        break
    if rowstr[:tlen] == target:
        rowstr = rowstr[tlen:]
        cnt += 1
    else:
        rowstr = rowstr[1:]

print(cnt)