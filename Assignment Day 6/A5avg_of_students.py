#Calculate avg marks of the student

def average(i):
    cnt = p = c = m = 0
    if (i['PHY'] != None):
        cnt += 1
        p = i['PHY']
    if (i['CHEM'] != None):
        cnt += 1
        c = i['CHEM']
    if (i['MATH'] != None):
        cnt += 1
        m = i['MATH']
    if cnt == 0:
        return 0
    return float(p+c+m)/cnt
student = {
    'A': {'PHY': 88, 'CHEM': 71, 'MATH': 88},
    'B': {'PHY': 52, 'CHEM': 99, 'MATH': 21},
    'C': {'PHY': 56, 'CHEM': 59, 'MATH': 28},
    'D': {'PHY': 15, 'CHEM': 61, 'MATH': 79},
    'E': {'PHY': 18, 'CHEM': 61, 'MATH': 82},
    'F': {'PHY': 41, 'CHEM': 70, 'MATH': 59},
    'G': {'PHY': None, 'CHEM': 61, 'MATH': 54},
    'H': {'PHY': 71, 'CHEM': None, 'MATH': 10},
    'I': {'PHY': 65, 'CHEM': 9, 'MATH': 65},
    'J': {'PHY': 69, 'CHEM': 39, 'MATH': 75},
    'K': {'PHY': 92, 'CHEM': 11, 'MATH': None},
    'L': {'PHY': None, 'CHEM': None, 'MATH': None}
}
for i in student.keys():
    student[i]['AVG'] = average(student[i])
for k, v in student.items():
    print('# Avg marks of student ', k, v['AVG'])