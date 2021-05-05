# section 02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# print에 대한 모든 옵션을 알아야 개발하는데 지장이 없다. 그러니 전부 작성해보자

# 기본출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''hello Python!''')
# 문자열을 출력할 때, 작은 따옴표 큰 따옴표 모두 쓸 수 있다.
# 따옴표 3개가 있어도 출력할 수가 있다.

print()

# Separator 옵션 사용
print('T', 'E', 'S', 'T', sep = '')
print('2019', '02', '19', sep = '-')
print('niceman', 'google.com', sep = '@')

# end 옵션 사용
print('Welcom To', end=' ')
print('the black parade', end=' ')
print('piano notes')
# print 끝이 줄바꿈이 되던것이 end값에 들어간 ' '공백값으로 바뀜

print()

# format 사용(개발할 때 많이사용)
# 1)
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You', 'Me'))
# .format({0}, {1}) 자동매핑되는 것을 알 수 있다.

# 2)
print("{a} are {b}".format(a='You', b='Me'))
# 중괄호 안에 변수로도 매핑이 가능

# 3)
print("%s's favorite number is %d" %('hyunseok', 3)) 
# %s : 문자
# %d : 일반 정수
# %f : 소수점실수
# 위 외에도 다른게 있다고 함.

# 1 > 2 > 3 순으로 명확하게 대상을 가리킨다.(명확한 코딩이 가능해짐)

print("Test1: %5d, Price: %4.2f" %(776, 6534.123))
print("Test1: {0: 5d}, Price:{1: 4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, price: {b:4.2f}".format(a=776, b=6534.123))

# escape 코드
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""

print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\')

print('\\you\\\n\n\n\n\n\n')
print('\t\t\ttest')
 