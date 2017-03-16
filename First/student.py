students = [{"id":20,"name":"anna","grade":6},
            {"id":30,"name":"tanq","grade":5},
            {"id":30,"name":"anna","grade":4},
            {"id":40,"name":"lena","grade":4},
            {"id":50,"name":"kate","grade":4},
            ]

def display(student):

    fmt = "{student_id}".format(student_id=student["id"])
    print(fmt)
    fmt = "[grade]".format(grade=student["grade"])
    print(fmt)
    for current_student in students:


        #if id > 30 and id < 50:
