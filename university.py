import sqlite3

database = sqlite3.connect('university.db')

cursor = database.cursor()


cursor.execute('''CREATE TABLE if not exists students
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER,
               major TEXT)''')

cursor.execute('''CREATE TABLE if not exists courses
               (course_id INTEGER PRIMARY KEY AUTOINCREMENT,
               course_name TEXT)''')

cursor.execute('''CREATE TABLE if not exists student_courses
               (
               student_id INTEGER ,
               course_id INTEGER, 
               PRIMARY KEY (student_id,course_id)
               FOREIGN KEY (student_id) REFERENCES students (id),
               FOREIGN KEY (course_id) REFERENCES courses (course_id))''')

while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")
    choice = input("Оберіть опцію (1-7): ")
    
    if choice == '1':
        name = input('Name:    ')
        age = input('Age:      ')
        cuourse = input('Course:     ')
        cursor.execute('''INSERT INTO students (name,age,major) VALUES (?,?,?)''',(name,age,cuourse))
        database.commit()
    elif choice == '2':
        course_name = input('Name course:     ')
        cursor.execute('''INSERT INTO courses (course_name) VALUES (?)''',(course_name,))
        database.commit()
    elif choice =="3":
        cursor.execute('''SELECT * FROM students''')
        list_students = cursor.fetchall()
        print(list_students)
    elif choice == "4":
        cursor.execute('''SELECT * FROM courses''')
        list_courses = cursor.fetchall()
        print(list_courses)
    elif choice == "5":
        student_id = input('Student id:      ')
        course_id = input('Course id:        ')
        cursor.execute('''SELECT * FROM students WHERE id = ?''', (student_id,))
        students_info = cursor.fetchall()
        cursor.execute('''SELECT * FROM courses WHERE course_id = ?''', (course_id,))
        cuourse_info = cursor.fetchall()
        if not students_info:
            print('Error student id')
        elif not cuourse_info:
            print('Error course id')
        else:
            try:
                cursor.execute('''INSERT INTO student_courses (student_id, course_id) VALUES (?,?)''',(student_id,course_id))
                database.commit()
            except sqlite3.IntegrityError:
                print('Student id is alredy exist')
                
    elif choice == '6':
        id = input('id:        ')
        cursor.execute('''SELECT student_id FROM student_courses WHERE course_id = ?''',(id,))
        students_id = cursor.fetchall()
        print(students_id)
    elif choice == "7":
        break
    else:
        print('error choice')
