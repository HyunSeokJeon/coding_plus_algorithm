# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈(정답은 영상)

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(len(q1))
print()

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print('\tapple;orange;banana;lemon')
print()

# 3. 화면에 * 기호 100개를 표시하세요.
print('*' * 100)
print()

# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
str_04 = '30'
print(type(str_04))
print(int(str_04))
print(float(str_04))
print(complex(str_04))
print(str(str_04))
print()

# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
str_05 = 'Niceman'
print('NO.1', str_05[4:7])
print('NO.3', str_05[4:])
print('NO.4', str_05[-3:])
print('NO.5', str_05[4:len(str_05)])
print('NO.6', str_05[str_05.index('m'):len(str_05)])
print()
# 추가답안
str_05_idx = str_05.index('man')
print(str_05[str_05_idx:str_05_idx+3])
print()

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
str_06 = 'Strawberry'
print(str_06[::-1]) # 외워둘 것
print(''.join(reversed(str_06)))
list_06 = list(str_06)
list_06.reverse()
print(''.join(list_06))

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
str_07 = '010-7777-9999'
print(str_07.replace('-', ''))

print(str_07[0:3]+str_07[4:8]+str_07[9:13])

# 정규표현식

import re

print(re.sub('[^0-9]', '', str_07))

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
str_08 = 'http://daum.net'
print(str_08[str_08.index('d'):])
print(str_08.replace('http://', ''))

# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
str_09 = 'Niceman'
print(str_09.upper())
print(str_09.lower())


# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
str_10 = 'abcdefghijklmn'
print(str_10[2 : 5])
print(str_10[-12 : -9])
print(str_10[str_10.index('c') : str_10.index('e') + 1])

# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
list_11 = ["Banana", "Apple", "Orange"]
list_11.remove('Apple')
print(list_11)
# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
tuple_12 = (1,2,3,4)
list_12 = list(tuple_12)
print(type(list_12))
print(list_12)
# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
dict_13 = {
    '성인' : 100000,
    '청소년' : 70000,
    '아동' : 30000
}
dict_ex = {}
dict_ex['성인'] = 100000
dict_ex['청소년'] = 70000
dict_ex['아동'] = 30000
print(type(dict_13))
print(dict_13)
print()

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
dict_14 = dict_13.copy()
dict_14['소아'] = 0
print(dict_14)
print()
print(dict_13)
# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
dict_15 = dict_13.copy()
print(dict_15.keys())

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
dict_16 = dict_13.copy()
print(dict_16.values())

# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***
