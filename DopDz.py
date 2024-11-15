grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}


a = students.pop()
b = students.pop()
c = students.pop()
d = students.pop()
e = students.pop()

print(a, b, c, d ,e)

student_ = [a, b, c, d, e]
student_.sort()
print(student_)
a = student_.pop(0)
b = student_.pop(0)
c = student_.pop(0)
d = student_.pop(0)
e = student_.pop(0)


one = grades.pop(0)
one_ = (sum(one)/len(one))
print(float(one_))

two = grades.pop(0)
two_ = (sum(two)/len(two))
print(float(two_))

three = grades.pop(0)
three_ = (sum(three)/len(three))
print(float(three_))

four = grades.pop(0)
four_ = (sum(four)/len(four))
print(float(four_))

five = grades.pop(0)
five_ = (sum(five)/len(five))
print(float(five_))

Dnevnik = {a:one_, b:two_, c:three_, d:four_, e:five_ }
print(Dnevnik)

