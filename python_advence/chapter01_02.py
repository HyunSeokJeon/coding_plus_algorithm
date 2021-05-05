# Chapter01_2
# 파이썬 심화
# 객체 지향 프로그래밍(oop) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 클래스 재 선언

class Student():
    """
    Student Class
    Author : Hyunseok
    Date : 2021.03.24
    """

    # 클래스 변수
    student_count = 0
    
    def __init__(self, name, number, grade, details, email=None): # email = None 선택 매개변수
        # 인스턴스 변수
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        Student.student_count += 1

    def __str__(self):
        return 'str : {}'.format(self._name)
    
    def __repr__(self):
        return 'repr : {}'.format(self._name)

    def detail_info(self):
        print('corrent Id : {}'.format(id(self)))
        print('student Detail Info : {} {} {}'.format(self._name, self._email, self._details))

    def __del__(self):
        Student.student_count -= 1



# Self 의미
stu1 = Student('Cho', 2, 3, {'gender' : 'Male', 'score1' : 65, 'score2': 44})
stu2 = Student('Chang', 4, 1, {'gender' : 'Female', 'score1' : 85, 'score2': 74}, 'stu2@naver.com')
# ID 확인
print(id(stu1))
print(id(stu2))

# 값비교
print(stu1._name == stu2._name)
# 레퍼런스(주소값?) 비교
print(stu1 is stu2)

# dir & dict 확인

print(dir(stu1))
print(dir(stu2))

print()
print()

print(stu1.__dict__)
print(stu2.__dict__)

# Docstring
print(Student.__doc__)
print()

# 실행
stu1.detail_info()
stu2.detail_info()

# 에러
# Student.detail_info()

# 인스턴스로만 접근할 수 있는것이 아닌 클래스로 접근해서 해당 메소드의 self값(매개변수)만 주면 실행가능
Student.detail_info(stu1)
Student.detail_info(stu2)

# 비교
print(stu1.__class__, stu2.__class__)
print(id(stu1.__class__) ==  id(stu2.__class__))

print()

# 인스턴스 변수
# 직접 접근(PEP 문법적으로 권장x)

print(stu1._name, stu2._name)
print(stu1._email, stu2._email)

print()
print()

# 클래스 변수

# 접근
print(stu1.student_count)
print(stu2.student_count)
print(Student.student_count)

print()
print()


# 공유 확인
print(Student.__dict__)
print(stu1.__dict__)
print(dir(stu1))

# 인스턴스 네임스페이스 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))
# 질문 dir(stu1)을 해보면 student_count가 있음 

del stu2

print(stu1.student_count)
print(Student.student_count)