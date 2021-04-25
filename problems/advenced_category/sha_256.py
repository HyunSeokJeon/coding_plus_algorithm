import hashlib

a = input()
b = a.encode()
c = hashlib.sha256(b).hexdigest()

print(c)