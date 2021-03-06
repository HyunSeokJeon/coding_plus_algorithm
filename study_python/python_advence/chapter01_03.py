# Chapter01_3
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스테이틱 메소드

# 기본 인스턴스 메소드

class Student(object):
    """
    Student Class
    Author : Jeon
    Date : 2021.03.24
    Description : Class, Static, Instance Method
    """

    # Class Variable
    tuition_per = 1.0
    
    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    # Instance Method
    def full_name(self):
        return '{}, {}'.format(self._first_name, self._last_name)

    # Instance Method
    def detail_info(self):
        return 'Student Detail Info : {}, {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa)

    # Instance Method
    def get_fee(self):
        return 'Before Tuition -> Id : {}, fee : {}'.format(self._id, self._tuition)

    # Instance Method
    def get_fee_culc(self):
        return 'After Tuition -> Id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition_per)

    # Instance Method
    def __str__(self):
        return 'Student Info -> name : {} grade : {} email : {}'.format(self.full_name(), self._grade, self._email)

    # Class Method
    @classmethod
    def raise_fee(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.tuition_per = per
        print('Succed! tuition increased!')

    # class Method
    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition * cls.tuition_per, gpa)

    # Static Method
    @staticmethod
    def is_scholarship_st(inst):
        if inst._gpa >= 4.3:
            return '{} is a scholarship recipient.'.format(inst._last_name)
        return 'Sorry. Not a scholarship recipient.'



# 학생 인스턴스
student1 = Student(1, 'Kim', 'Sarang', 'student1@naver.com', 1, 400, 3.5)
student2 = Student(2, 'Lee', 'Myungho', 'student2@daum.net', 2, 500, 4.3)

# 기본정보
print(student1)
print(student2)

# 전체 정보
print(student1.detail_info())
print(student2.detail_info())

# 학비 정보(인상 전)
print(student1.get_fee())
print(student2.get_fee())

print()

# 학비 인상(클래스 메소드 미사용)
# Student.tuition_per = 1.2

# 학비 인상(클래스 메소드 사용)
Student.raise_fee(1.3)


# 학비 정보(인상 후)
print(student1.get_fee_culc())
print(student2.get_fee_culc())

# 클래스 메소드 인스턴스 생성 실습
student3 = Student.student_const(3, 'Park', 'Minji', 'Student3@gmail.com', 3, 550, 4.5)
student4 = Student.student_const(4, 'Cho', 'Sunghan', 'Student4@gmail.com', 4, 600, 4.1)

# 전체 정보

print(student3.detail_info())
print(student4.detail_info())
print()

# 학생 학비 변경 확인

print(student3._tuition)
print(student4._tuition)
print()

# 장학금 혜택 여부(스테이틱 메소드 미사용)
def is_scholarship(inst):
    if inst._gpa >= 4.3:
        return '{} is a scholarship recipient.'.format(inst._last_name)
    return 'Sorry. Not a scholarship recipient.'


print(is_scholarship(student1))
print(is_scholarship(student2))
print(is_scholarship(student3))
print(is_scholarship(student4))


print()
print()


# 장학금 혜택 여부(스테이틱 메소드 사용)
print(Student.is_scholarship_st(student1))
print(Student.is_scholarship_st(student2))
print(Student.is_scholarship_st(student3))
print(Student.is_scholarship_st(student4))

print()

print(student1.is_scholarship_st(student1))
print(student2.is_scholarship_st(student2))
print(student3.is_scholarship_st(student3))
print(student4.is_scholarship_st(student4))










