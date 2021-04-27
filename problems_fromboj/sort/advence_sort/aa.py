a = dict()
from collections import defaultdict

a = {1: {2: 4, 3: 3}, 2: {1: 4, 3: 2}, 3: {1: 3, 2: 2}}

print(list(a.get(1).keys()))