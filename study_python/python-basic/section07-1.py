# Section07-1
# 파이썬 클래서 상세 이해
# Self, 클래스, 인스턴스 변수

# # 선언
# class 클래스명:
#     함수
#     함수
#     함수

# 예제1
# 클래스 첫 글자는 대문자
    
# 클래스를 선언하고 pass를 넣으면 구현된것이 없어도 에러가 발생하지 않는다.

class UserInfo:
    # 속성, 메소드
    def __init__(self, name): # 클래스를 최초 초기화
        self.name = name

    def user_info_p(self):
        print("name : ", self.name)

# 네임스페이스
user1 = UserInfo("Kim")
print(user1.name)
user1.user_info_p()
user2 = UserInfo("Park")
print(user2.name)
user2.user_info_p()

print(id(user1))
print(id(user2))
# 2112281255888
# 2112281255792
# 서로다른 id를 가지고 있음을 알 수 있다. 서로다른 네임스페이스를 가지고 있다는 것

print(user1.__dict__)
print(user2.__dict__)

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생상
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용
# 위에 user1 = UserInfo("Kim") 이것이 인스턴스 생성한 과정

# 예제2
# self의 이해
class SelfTest:
    # 클래스 메소드
    def function1():
        print('function1 called!')
    # 인스턴스 메소드
    def function2(self):
        print(id(self))
        print('function2 called!')

self_test = SelfTest()
# self_test.function1()
SelfTest.function1()
# self인자를 안받으므로 인스턴스를 생성해서 호출할 수 없고
# 클래스를 호출해서 그 안의 function1(클래스 메소드)을 직접 호출해야 한다.
self_test.function2()

print(id(self_test))
# SelfTest.function2()
# 오류 셀프인자가 없어서
SelfTest.function2(self_test)

# 예제3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    # 클래스 변수
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) # 클래스 네임스페이스, 클래스 변수(공유)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num)
# 인스턴스 네임스페이스에 없으면 클래스 네임스페이스로 가서 찾는다.
del user1

print(user2.stock_num)
print(user3.stock_num)









