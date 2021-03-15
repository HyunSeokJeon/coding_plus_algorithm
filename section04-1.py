# Section04-1
# 파이썬 데이터 타입

# 파이썬 데이터 타입 종류

# Boolean 1 0


# Numbers

# List
# Tuples
# Sets
# Dictionaries


v_str1 = 'Niceman'
v_bool = True
v_str2 = 'Goodboy'
v_float = 10.3
v_int = 7
v_dict = {
    'name' : 'kim',
    'age' : 25    
}

v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}


print(type(v_str1))
print(type(v_bool))
print(type(v_str2))
print(type(v_float))
print(type(v_int))
print(type(v_dict))
print(type(v_set))
print(type(v_tuple))

i1 = 39
i2 = 939
big_int1 = 999999999999999999999999999999999999999999999999
big_int2 = 777777777777777777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(big_int1 - big_int2)
print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print (i2 + f3)

result = f3 + i2
print(result, type(result))

a = 5.
b = 4
c = 10

print(type(a), type(b))

result2 = a + b
print(result2, type(result2))

# 형변환
# int, float, complex(복소수)

print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))
# 유연한 형변환이 가능하다는것이 파이썬의 장점!
print(complex(False))

