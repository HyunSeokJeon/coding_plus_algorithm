# Chapter01_1
# 파이썬 심화
# 객체 지향 프로그래밍(oop) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 일반적인 코딩

# 학생1
student_name_1 = 'Kim'
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [
    {'gender' : 'Male'},
    {'score1' : 95},
    {'score2' : 88}
]

# 학생2
student_name_2 = 'Lee'
student_number_2 = 2
student_grade_2 = 2
student_detail_2 = [
    {'gender' : 'Female'},
    {'score1' : 72},
    {'score2' : 82}
]

# 학생3
student_name_3 = 'Park'
student_number_3 = 3
student_grade_3 = 4
student_detail_3 = [
    {'gender' : 'Male'},
    {'score1' : 99},
    {'score2' : 100}
]


# 리스트 구조
# 관리하기 불편
# 데이터의 정확한 위치(인덱스)매핑 해서 사용
student_names_list = ['kim', 'Lee', 'Park']
student_numbers_list = [1,2,3]
student_grades_list = [1, 2, 4]
student_details_list = [
    {'gender' : 'Male', 'score1' : 95, 'score2' : 88},
    {'gender' : 'Female', 'score1' : 72, 'score2' : 82},
    {'gender' : 'Male', 'score1' : 99, 'score2' : 100}
]

# 학생 삭제
del student_names_list[1]
del student_numbers_list[1]
del student_grades_list[1]
del student_details_list[1]

print(student_names_list)
print(student_numbers_list)
print(student_grades_list)
print(student_details_list)

print()
print()


# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제
students_dicts = [
    {'student_name' : 'Kim', 'student_number' : 1, 'student_grade' : 1, 'student_detail' : {'gender' : 'Male', 'score1' : 95, 'score2' : 88}},
    {'student_name' : 'Lee', 'student_number' : 2, 'student_grade' : 2, 'student_detail' : {'gender' : 'Female', 'score1' : 72, 'score2' : 82}},
    {'student_name' : 'Park', 'student_number' : 3, 'student_grade' : 4, 'student_detail' : {'gender' : 'Male', 'score1' : 99, 'score2' : 100}}
]

del students_dicts[1]
print(students_dicts)
print()
print()


# 클래스 구조
# 구조 설계 후 재사용성 증가 코드 반복 최소화, 메소드 활용

class Student():
    def __init__(self, name, number, grade, details):
        self.name = name
        self.number = number
        self.grade = grade
        self.details = details

    def __str__(self):
        return 'str : {} - {}'.format(self.name, self.number)

    def __repr__(self):
        return 'repr : {} - {}'.format(self.name, self.number)

    
student1 = Student('Kim', 1, 1, {'gender' : 'Male', 'score1' : 95, 'score2': 88})
student2 = Student('Lee', 2, 2, {'gender' : 'Female', 'score1' : 72, 'score2': 82})
student3 = Student('Park', 3, 4, {'gender' : 'Male', 'score1' : 99, 'score2': 100})

print(student1.__dict__)
print(student2.__dict__)
print(student3.__dict__)
# 파이썬의 모든 객체는 딕셔너리 기반으로 만들어져 있어서 .__dict__으로 확인

# 리스트 선언
students_list = []
students_list.append(student1)
students_list.append(student2)
students_list.append(student3)

print()

print(students_list)


for student in students_list:
    print(repr(student))
    print(student)

# 출력 결과
# str : Kim
# str : Lee
# str : Park
# Student() 클래스의 __str__를 오버라이드해서 위와 같이 원하는 메세지를 볼 수 있게 함




