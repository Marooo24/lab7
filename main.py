from btu.data import b_names, g_names, last_names, subject
import random

full_name = ''
names_list = []
COUNT = 1000

for i in range(COUNT):
    random_number = random.randint(0,1)
    if random_number:
        full_name = b_names[random.randint(0, len(b_names)-1)]
    else:
        full_name = g_names[random.randint(0, len(g_names)-1)]
    full_name += " " + last_names[random.randint(0, len(last_names)-1)]
    names_list.append(full_name)

student_info = []
for i in range(1000000):
    student_info.append({'full_name': names_list[random.randint(0, COUNT-1)],
                         'subject': subject[random.randint(0, len(subject)-1)],
                         'score': random.randint(1, 100)})

merged_student_info = []
names_list = list(set(names_list))
for students in student_info:
    if list(students.values())[0] in names_list:
        merged_student_info.append({'full_name': list(students.values())[0],
                                   'subject': {list(students.values())[1]: [students['score']]}})
        del names_list[names_list.index(list(students.values())[0])]
    else:
        for i in merged_student_info:
            if list(students.values())[0] in list(i.values()):
                if list(students.values())[1] in list(i['subject'].keys()):
                    i['subject'][list(students.values())[1]].append(students['score'])
                else:
                    i['subject'][list(students.values())[1]] = [students['score']]
                break

highest = 0
gpa_students = ''
for i in merged_student_info:
    i['avg'] = []
    for j in i['subject']:
        i['avg'].append(sum(i['subject'][j])/len(i['subject'][j]))
    i['gpa'] = sum(i['avg'])/len(i['avg'])
    if i['gpa'] > highest:
        highest = i['gpa']

for i in merged_student_info:
    if i['gpa'] == highest:
        print(i['full_name'], highest)




