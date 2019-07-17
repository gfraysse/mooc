# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division
from collections import namedtuple

n = int(raw_input())
columns = raw_input().split()
Student = namedtuple('Student',columns)
Students = []
sum_marks = 0
        
for i in range(n):
    student = Student._make(raw_input().split())
    Students.append(student)
    sum_marks += int(student.MARKS)

value = sum_marks / len(Students)
print("%.2f" % value)
