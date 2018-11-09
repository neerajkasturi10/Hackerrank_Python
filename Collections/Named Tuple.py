from collections import namedtuple
N = int(input())
col_names = namedtuple('col_names',input().split())
total = 0
for i in range(N):
    stud_details = input().split()
    student = col_names(stud_details[0], stud_details[1], stud_details[2], stud_details[3])
    total += int(student.MARKS)
avg = total/N
print(avg)