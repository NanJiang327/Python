def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))

for x in range(0):
    print(x)

class Student:
    pass

def set_age(self, age):
    self.age = age


Student.set_age = set_age

s = Student()
s2 = Student()

s.set_age(12)
print(s.age)
s2.set_age(15)
print(s2.age)