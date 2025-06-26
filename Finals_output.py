from tabulate import tabulate

num_students = 0
all_names = []
sem = ["Midterm", "Finals"]
all_studentsData = {"Midterm": [], 
                    "Finals": []}

students_grades = {"Midterm": [],
                    "Finals" :[]}
grade_points = {"Midterm": [],
                 "Finals" :[]}
all_equivalents = {"Midterm": [],
                    "Finals" :[]}
students_semester_grade = []
semester_points = []
semester_equivalents = []


student_num = 1
# grade convertion
class Student:
    def __init__(self, 
                 name, 
                 all_assignments, 
                 all_seatworks, 
                 all_quizzes, 
                 midterm_exam, 
                 total_ass, 
                 total_sw, 
                 total_quiz, 
                 assignment_grade, 
                 seatwork_grade, 
                 quiz_grade, 
                 classStanding, 
                 midterm_grade, 
                 midtermFinal_grade):
        self.name = name
        self.all_assignments = all_assignments
        self.all_seatworks = all_seatworks
        self.all_quizzes = all_quizzes 
        self.midterm_exam = midterm_exam
        self.total_ass = total_ass
        self.total_sw = total_sw
        self.total_quiz = total_quiz
        self.assignment_grade = assignment_grade
        self.seatwork_grade = seatwork_grade
        self.quiz_grade = quiz_grade
        self.classStanding = classStanding
        self.midterm_grade = midterm_grade
        self.midtermFinal_grade = midtermFinal_grade
def convertion(grade):
    if grade >= 97 or grade == 100:
        equivalent = "Excellent"
        return 1.00, equivalent
    elif grade >= 94 or grade == 96:
        equivalent = "Excellent"
        return 1.25, equivalent
    elif grade >= 91 or grade == 93:
        equivalent = "Very Good"
        return 1.50, equivalent
    elif grade >= 88 or grade == 90:
        equivalent = "Very Good"
        return 1.75, equivalent
    elif grade >= 85 or grade == 87:
        equivalent = "Good"
        return 2.00, equivalent
    elif grade >= 82 or grade == 84:
        equivalent = "Good"
        return 2.25, equivalent
    elif grade >= 79 or grade == 81:
        equivalent = "Satisfactory"
        return 2.50, equivalent
    elif grade >= 76 or grade == 78:
        equivalent = "Satisfactory"
        return 2.75, equivalent
    elif grade == 75:
        equivalent = "Passing"
        return 3.00, equivalent
    elif grade >= 65 or grade == 74:
        equivalent = "Conditional"
        return 4.00, equivalent
    else:
        equivalent = "Failed"
        return 5.00, equivalent

# Show all data
def show_all_data(num_students):
    print("\n============================ Full Report ============================\n")
    for semester in sem:
        if not all_studentsData[semester]:
            print(f"No data available for {semester} semester.")
            continue  # Skip if no data for the semester

        print(f"\n----------------------------- {semester} Grades -----------------------------\n")
        i = 0
        for student in all_studentsData[semester]:
            print(f"Name : {student.name}")
            print(f"List Assignments: {student.all_assignments}")
            print(f"Total Assignments: {student.total_ass}")
            print(f"Asignment Equivalent Grade: {student.assignment_grade}\n")
            print(f"List Seatwork: {student.all_seatworks}")
            print(f"Total Seatwork: {student.total_sw,}")
            print(f"Seatwork Equivalent Grade: {student.seatwork_grade}\n")
            print(f"List Quizzes: {student.all_quizzes}")
            print(f"Total Quizzes: {student.total_quiz}")
            print(f"Quiz Equivalent Grade: {student.quiz_grade}\n")
            print(f"Class Standing: {student.classStanding}\n")
            print(f"{semester} Exam: {student.midterm_exam}")
            print(f"{semester} Equivalent Grade: {student.midterm_grade}\n")
            print(f"{semester} Grade: {student.midtermFinal_grade}\n")
            print(f"{semester} point: {grade_points[semester][i]}")
            print(f"Point equivalent: {all_equivalents[semester][i]}\n")
            print("___________________________________________________________________________")
            i += 1
    print(f"\n----------------------------- Semester Grades -----------------------------\n")
    if students_semester_grade == []:
        print("No data available for Semester Grade.")
         
    for m in range(num_students):
        print(f"Name : {all_names[m]}")
        print(f"Semester Grade: {students_semester_grade[m]}")
        print(f"Semester point: {semester_points[m]}")
        print(f"Equivalent: {semester_equivalents[m]}\n")

def search_student(stu_name, what_sem):
    found = False
    for semester in what_sem:
        i = 0
        for student in all_studentsData[what_sem]:
            if student.name.lower() == stu_name.lower():
                found = True
                print(f"\n----------------------------- {semester} Grades -----------------------------\n")
                print(f"Name : {student.name}")
                print(f"List Assignments: {student.all_assignments}")
                print(f"Total Assignments: {student.total_ass}")
                print(f"Asignment Equivalent Grade: {student.assignment_grade}\n")
                print(f"List Seatwork: {student.all_seatworks}")
                print(f"Total Seatwork: {student.total_sw,}")
                print(f"Seatwork Equivalent Grade: {student.seatwork_grade}\n")
                print(f"List Quizzes: {student.all_quizzes}")
                print(f"Total Quizzes: {student.total_quiz}")
                print(f"Quiz Equivalent Grade: {student.quiz_grade}\n")
                print(f"Class Standing: {student.classStanding}\n")
                print(f"{semester} Exam: {student.midterm_exam}")
                print(f"{semester} Equivalent Grade: {student.midterm_grade}\n")
                print(f"{semester} Grade: {student.midtermFinal_grade}\n")
                print(f"{semester} point: {grade_points[semester][i]}")
                print(f"Point equivalent: {all_equivalents[semester][i]}\n")
                print("\n---------------------------------------------------------------------------------")
            i += 1
    if found == False:
        print(f"\nStudent named '{stu_name}' not found in selected semester(s).")

# main run
while True:
    try:
        print("=================================================================================\n")
        print("                             Semester Grades Calculator\n")
        print("[1]Continue For Using Calculator"
              "\n[2]Show Student Data"
              "\n[3]Show all Student Data"
              "\n[4]Show Solution Base"
              "\n[5]Clear all Student Data"
              "\n[6]Exit")
        print("\n---------------------------------------------------------------------------------")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            while True:
                try:
                    if num_students == 0:
                        new_num_students = int(input("\nEnter the number of students: ")) 
                        if new_num_students <= 0:
                            print("Invalid Input: Please enter a positive integer.\n")
                            continue
                        elif new_num_students > 30:
                            print("Invalid Input: No. of student do not exceed 30")
                            continue
                        start_index = 0
                        num_students = new_num_students
                    else:
                        new_num_students = int(input("\nEnter the number of students to add: ")) 
                        if new_num_students <= 0:
                            print("Invalid Input: Please enter a positive integer.\n")
                            continue
                        elif (num_students + new_num_students) > 30:
                            print("Invalid Input: Total number of students cannot exceed 30.")
                            continue
                        start_index = num_students
                        num_students += new_num_students
                    break
                except ValueError:
                    print("Invalid Input: Please enter a valid integer.\n")
              
            nameloop = 0
            # loop for each semester
            for v in range(len(sem)):
                semester = sem[v]
                name_ver = num_students
                while True:
                    try:
                        num_ass = int(input(f"\nEnter the number of assignment in {semester} you want to add: "))
                        if num_ass <= 0:
                            print("Invalid Input: Please enter a positive integer.\n")
                        elif num_ass > 10:
                            print("Invalid Input: No. of assignemnt do not exceed 10.\n")
                        else:
                            print("\n---------------------------------------------------------------------------------")
                            break
                    except ValueError:
                        print("Invalid Input: Please enter a valid integer.")
                while True:
                    try:
                        num_sw = int(input(f"\nEnter the number of seatwork in {semester} you want to add: "))
                        if num_sw <= 0:
                            print("Invalid Input: Please enter a positive integer.\n")
                        elif num_sw > 10:
                            print("Invalid Input: No. of Seatwork do not exceed 10.\n")
                        else:
                            print("\n---------------------------------------------------------------------------------")
                            break
                    except ValueError:
                        print("Invalid Input: Please enter a valid integer.\n")
                while True:
                    try:
                        num_quizzes = int(input(f"\nEnter the number of quiz in {semester} you want to add: "))
                        if num_quizzes <= 0:
                            print("Invalid Input: Please enter a positive integer.\n")
                        elif num_quizzes > 10:
                            print("Invalid Input: No. of quizzes do not exceed 10.\n")
                        else:
                            print("\n---------------------------------------------------------------------------------")
                            break
                    except ValueError:
                        print("Invalid Input: Please enter a valid integer.")
                
                #getting midterm each student grades
                for i in range(start_index, start_index + new_num_students):
                    all_assignments = []
                    all_seatworks = []
                    all_quizzes = []
                    
                    # name input
                    if nameloop != 1: 
                        if num_students > 0:
                            while True:
                                try:
                                    name = input(f"\nEnter the name of student no.{student_num}: ").strip()
                                    all_names.append(name)
                                    name_ver -= 1
                                    student_num += 1
                                    break
                                except:
                                    print("Invalid Input: Please enter a valid name.\n")
                    #getting Student raw grades
                    # Assignments
                    print("\n==================================Grade Input===================================")
                    print(f"\nEnter the grades for {semester} of {all_names[i]}\n")
                    print("---------------------------------------------------------------------------------\n")
                    print("                                  Assignments\n")
                    print("---------------------------------------------------------------------------------\n")
                        
                    for j in range(num_ass):
                        while True:
                            try:
                                assignment = float(input(f'Enter your grade for assignment {j + 1}: '))
                                if assignment < 0:
                                    print("Invalid Input: Please enter a positive integer.\n")
                                elif assignment > 100:
                                    print("Invalid Input: Grade cannot be above 100.\n")
                                elif assignment <= 49:
                                    print("Invalid Input: Grade cannot below 50.\n")
                                else:
                                    all_assignments.append(assignment)
                                    break
                            except:
                                print("Invalid Input: Please enter only INTEGERS.")
                    total_ass = sum(all_assignments)
                    print("Your total assignement: ", total_ass)
                    print("\n---------------------------------------------------------------------------------\n")
                    
                    # Seatwork grades
                    print("                                 Seatworks\n")
                    print("---------------------------------------------------------------------------------\n")
                    for k in range(num_sw):
                        while True:
                            try:
                                seatwork = float(input(f'Enter your grade for seatwork {k + 1}: '))
                                if seatwork < 0:
                                    print("Invalid Input: Please enter a positive integer.")
                                elif seatwork > 100:
                                    print("Invalid Input: Grade cannot be above 100.")
                                elif seatwork <= 49:
                                    print("Invalid Input: Grade cannot below 50.")
                                else:
                                    all_seatworks.append(seatwork)
                                    break
                            except:
                                print("Invalid Input: Please enter only INTEGERS.")
                    total_sw = sum(all_seatworks)
                    print("Your total seatwork: ", total_sw)
                    print("\n---------------------------------------------------------------------------------\n")

                    # Quiz grades
                    print("                                  Quizzes\n")
                    print("---------------------------------------------------------------------------------\n")
                    for l in range(num_quizzes):
                        while True:
                            try:
                                quiz = float(input(f'Enter your grade for quiz {l + 1}: '))
                                if quiz < 0:
                                    print("Invalid Input: Please enter a positive integer.")
                                elif quiz > 100:
                                    print("Invalid Input: Grade cannot be above 100.")
                                elif quiz <= 49:
                                    print("Invalid Input: Grade cannot below 50.")
                                else:
                                    all_quizzes.append(quiz)
                                    break
                            except:
                                print("Invalid Input: Please enter only INTEGERS.")
                    total_quiz = sum(all_quizzes)
                    print("Your total quiz: ", total_quiz)
                    print("\n---------------------------------------------------------------------------------\n")

                    # Midterm Exam
                    print(f"                               {semester} Exam\n")
                    print("---------------------------------------------------------------------------------\n")
                    while True:
                        try:
                            midterm_exam = float(input(f"\nEnter your {semester}' grade: "))
                            if midterm_exam < 0:
                                print("Invalid Input: Please enter a positive integer.")
                            elif midterm_exam > 100:
                                print("Invalid Input: Grade cannot be above 100.")
                            elif midterm_exam <= 49:
                                print("Invalid Input: Grade cannot below 50.")
                            else:
                                break
                        except ValueError:
                            print("Invalid Input: Please enter only INTEGERS.")

                    # Computation
                    assignment_grade = (total_ass / num_ass) * 0.2
                    seatwork_grade = (total_sw / num_sw) * 0.2
                    quiz_grade = (total_quiz / num_quizzes) * 0.6
                    classStanding = (assignment_grade + seatwork_grade + quiz_grade) * 0.7
                    midterm_grade = midterm_exam * 0.3
                    midtermFinal_grade = classStanding + midterm_grade
                    
                    # choice if want to see raw
                    print("\n-----------------------------------------------------")
                    while True:
                        try:
                            showRaw = int(input("\nYou want to see the Raw Data? \n[1]Yes : [2]No: "))
                            if showRaw == 1:
                                # Raw data tabled
                                print("\n================================= Raw data =====================================\n")
                                table_rawData = []
                                table_rawData.append([all_names[i], all_assignments, all_seatworks, all_quizzes])
                                table_rawData.append(["Total", total_ass, total_sw, total_quiz, midterm_exam])
                                header_rawData = ["Name", "Assigments", "Seatworks", "Quizzes", f"{semester} Exam"]
                                print(tabulate(table_rawData, headers=header_rawData, tablefmt="psql", colalign=("left","center","center", "center", "center")))
                                break
                            elif showRaw == 2:
                                print("Skipping raw data display.")
                                break
                            else:
                                print("Invalid Input: Please enter 1 or 2.")
                        except ValueError:
                            print("Invalid Input: Please enter only INTEGERS.")
                            
                    # Converted Grade
                    convertion_grade, equivalent = convertion(midtermFinal_grade)
                    grade = round(convertion_grade, 2)

                    print("\n================================= Computed data =================================\n")
                    table_computedData = []
                    table_computedData.append([all_names[i], classStanding, midterm_grade])
                    header_table_computedData = ["Name", "ClassStanding", f"{semester} Exam Grade"]
                    print(tabulate(table_computedData, headers=header_table_computedData, tablefmt="rst", colalign=("left","center","center")))
                    
                    print(f"{all_names[i]}, your {semester} Grade is {midtermFinal_grade:.2f}")
                    print(f"Your Grade Point is {grade} and Equivalent is {equivalent}\n")
                    print("\n=================================================================================\n")

                    

                    # add to lists
                    students_grades[semester].append(midtermFinal_grade)
                    grade_points[semester].append(grade)
                    all_equivalents[semester].append(equivalent)

                    #use class
                    student_data = Student(all_names[i], 
                                        all_assignments, 
                                        all_seatworks, 
                                        all_quizzes, 
                                        midterm_exam, 
                                        total_ass, 
                                        total_sw, 
                                        total_quiz, 
                                        assignment_grade, 
                                        seatwork_grade, 
                                        quiz_grade, 
                                        classStanding, 
                                        midterm_grade, 
                                        midtermFinal_grade)
                    all_studentsData[semester].append(student_data)

                
                while True:
                    try:
                        showSummary = int(input(f"\nYou want to show the summary of {semester}\n [1]Yes : [2]No: "))
                        if showSummary == 1:
                            # show summary
                            print("\n====================================== Summary ==================================\n")
                            table_summary = []
                            for i in range(num_students):
                                table_summary.append([
                                    all_names[i], 
                                    f"{students_grades[semester][i]:.2f}", 
                                    grade_points[semester][i], 
                                    all_equivalents[semester][i]])
                            headers_summary = ["Name", f"{semester} Grade", "Grade Point", "Equivalent"]
                            print(tabulate(table_summary, headers=headers_summary, tablefmt="psql", colalign=("left","center","center", "center")))
                            break
                        elif showSummary == 2:
                            print("Skipping summary display.")
                            break
                        else:
                            print("Invalid Input: Please enter 1 or 2.")
                    except ValueError:
                        print("Invalid Input: Please enter only INTEGERS.")
                # Reset student_num for next semester
                nameloop += 1
            # semester computation
            students_semester_grade.clear()
            semester_points.clear()
            semester_equivalents.clear()
            semester_table_grade = []
            for i in range(num_students):
                semester_finalGrade = (students_grades["Finals"][i] + students_grades["Midterm"][i]) / 2
                students_semester_grade.append(semester_finalGrade)

                #convertion
                convertion_grade, equivalent = convertion(semester_finalGrade)
                semester_points.append(convertion_grade)
                semester_equivalents.append(equivalent)
                #create table
                semester_table_grade.append([
                    all_names[i], students_semester_grade[i], semester_points[i], semester_equivalents[i]
                ])
                
            # show semester grade
            print("====================================== SEMESTER GRADE ==================================\n")
            header_semester_grade = ["Name", "Semester Grade", "Points", "Equivalent"]
            print(tabulate(semester_table_grade, headers=header_semester_grade, tablefmt="psql", colalign=("left","center","center", "center")))
        elif choice == 2:
            if all_names == []:
                print("There is no Data, Please choose 1 First")
            else: 
                student_name = input("Enter the exact student name: ")
                print("Please choose what semester you want to see"
                    "\n [1]Midterm"
                    "\n [2]Finals"
                    "\n [3]Both" )
                while True:
                    try:
                        sem_search = int(input("Please enter your Choice: "))
                        if sem_search == 1:
                            sem_tosearch = ["Midterm"]
                            search_student(student_name, sem_tosearch)
                            break
                        elif sem_search == 2:
                            sem_tosearch = ["Finals"]
                            search_student(student_name, sem_tosearch)
                            break
                        elif sem_search == 3:
                            sem_tosearch = ["Midterm", "Finals"]
                            search_student(student_name, sem_tosearch)
                            break
                        else:
                            print("Invalid: Output: Please Enter only on the choices.")
                            continue
                    except ValueError:
                        print("Invalid Input: Please enter only INTEGERS.")
            
        elif choice == 3:
            show_all_data(num_students)
        elif choice == 4:
            print("\nMIDTERM/FINALS GRADE")
            print ("Class Standing : 70%")
            print ("Midterm Exam   : 30%")
            print ("                -----")
            print ("Total          :100%\n")
            print ("______________________________________________________")
            print ("\nClass Standing Grade")
            print ("Assignment :  20%")
            print ("Seat Work  :  20%")
            print ("Quiz       :  60%")
            print ("             -----")
            print ("Total      : 100%\n")
            print ("______________________________________________________")
            print ("\nSEMESTER GRADE")
            print ("Midterm Grade  :  50%")
            print ("Finals Grade   :  50%")
            print ("                -----")
            print ("Total          : 100%\n")
        elif choice == 5:
            confirm = input("Are you sure you want to clear all data? (y/n): ").strip()
            if confirm == 'y':
                all_names.clear()
                for semester in sem:
                    all_studentsData[semester].clear()
                    students_grades[semester].clear()
                    grade_points[semester].clear()
                    all_equivalents[semester].clear()
                students_semester_grade.clear()
                semester_points.clear()
                semester_equivalents.clear()
                student_num = 1
                num_students = 0
                print("All student data has been cleared.\n")
            else:
                print("Clear data canceled.\n")
        elif choice == 6:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
    except:
        print("An error occurred. Please try again.")
        continue