# Week02-report
# 둘째주 과제

# 1번문제
import csv

with open('./a.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    a = [10, 60, 20, 33, 55, 25, 64, 83, 523, 54, 87, 84, 56, 84]
    writer.writerow(a)
with open('./a.csv', 'r') as f:
    reader = csv.reader(f)
    ans = sum(int(strNum) for line in reader for strNum in line)
    print(ans)


# 2번 문제
class Median:
    def __init__(self):
        self.itemList = []
        return

    def get_item(self, item):
        self.itemList.append(item)

    def clear(self):
        self.itemList.clear()

    def show_result(self):
        a = self.itemList
        b = int(a.__len__() / 2)
        print((sorted(a)[b] + sorted(a, reverse = True)[b]) / 2)


median = Median()
for x in range(10):
    median.get_item(x)
median.show_result()

median.clear()
for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
    median.get_item(x)
median.show_result()


# 3번 문제
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' cannot speak.')

    def move(self):
        print(self.name + ' cannot move.')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print(self.name + ' moves like a jagger.')


class Retriever(Dog):
    def __Init__(self, name):
        super().__init__(name)

    def speak(self):
        print(self.name + ' is smart enough to speak.')


dog = Dog('Nancy')
dog.speak()
dog.move()

super_dog = Retriever('Michael')
super_dog.speak()
super_dog.move()


# 4번 문제
class Foo:
    bar = 'A'

    def __init__(self):
        self.bar = 'B'

    class Bar:
        bar = 'C'

        def __init__(self):
            self.bar = 'D'


print(Foo.bar)          # A 출력
print(Foo().bar)        # B 출력
print(Foo.Bar.bar)      # C 출력
print(Foo.Bar().bar)    # D 출력
