#Given students and their marks in following format calculate average marks for every subject

def average(tot, cnt):
    return float(tot)/cnt
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
p = c = m = 0.0
cnt_p = cnt_c = cnt_m = 0
for i in student.keys():
    if(student[i]['PHY'] != None):
        p += student[i]['PHY']
        cnt_p += 1
    if(student[i]['CHEM'] != None):
        c += student[i]['CHEM']
        cnt_c += 1
    if(student[i]['MATH'] != None):
        m += student[i]['MATH']
        cnt_m += 1
print('# Average PHY Marks : ', average(p, cnt_p))
print('# Average CHEM Marks : ', average(c, cnt_c))
print('# Average MATH Marks : ', average(m, cnt_m))