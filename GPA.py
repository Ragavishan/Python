def grade_to_gpa(grade):
    switcher={
            'A'=4.0,
            'B'=3.0,
            'C'=2.0,
            'D'=1.0,
            'F'=0.0
            }
    return switcher.get(grade,"Invalid grade")
print(grade_to_gpa('B'))
print(grade_to_gpa('G'))

    