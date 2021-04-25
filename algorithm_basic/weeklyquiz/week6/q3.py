nums = [1, 0, -1, 0, -2, 2]
target = 0
answer = list()
for a in range(len(nums)):
    for b in range(a+1, len(nums)):
        for c in range(b+1, len(nums)):
            for d in range(c+1, len(nums)):
                if (nums[a] + nums[b] + nums[c] + nums[d]) == target:
                    lista = [nums[a], nums[b], nums[c], nums[d]]
                    lista.sort()
                    answer.append(lista)
print(answer)