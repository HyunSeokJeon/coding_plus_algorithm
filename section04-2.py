# Section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am Boy."
str2 = 'NiceMan'

print(len(str1))
print(len(str2))

# 공백도 길이에 포함

# 빈 문자열도 선언이 가능
str3 = ""
print(len(str3))

# 문자열로 형변환해서 선언도 가능
str4 = str(1)
print(type(str4), len(str4))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab\ta"
print(escape_str2)

# Raw String
# escape 적용이 안됨
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인
# 변수 = \
# 줄바꾸고 내용을 쓰면 그대로 읽어냄
multi = \
""" 
문자열 
멀티라인 
테스트 
"""
print(multi)

# 문자열 연산
str_o1 = "*"
str_o2 = "abc"
str_o3 = "def"
str_o4 = "Nicemam"

print(str_o1 * 100)
print(str_o2 + str_o3)
print("a" in str_o4)
print("f" in str_o4)
print("z" not in str_o4)
print("n" in str_o4)
# 대소문자도 구분

# 문자열 형 변환
print(str(77) + "a")
print(str(10.4))


# 문자열 함수

# a = 'niceman'
# b = 'orange'

# print(a.islower())
# print(b.endswith('e'))
# print(a.capitalize())
# print(a.upper())
# print(a.replace('nice', 'good'))
# print(list(reversed(a)))


# 슬라이스 처리

# 문자열을 한번 할당하면 반환이 불가능하다


a = 'niceman'
b = 'orange'

print(a[0:3])
print(a[0:4])
print(a[0:7])
# 이렇게 쓰기보다는 
print(a[0:len(a)])
# a의 길이만큼을 함수로 써주는게 좋다

print(a[:4])
print(a[:])

print(b[0:4:2])
print(b[::2])

print(b[1:-2])
# o r a n  g e 이렇게 계산이 된다고 한다.   
# 0(1    )-2-1    
print(b[::-1])







