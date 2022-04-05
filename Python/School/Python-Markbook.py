 ##################
# ────▓▓▓▓▓▓──────  #
# ───▓▄▓▓▓▓▓▓─────  #
# ──────▓▓▓▓▓─▒▒──  #
# ─▓▓▓▓▓▓▓▓▓──▒▒▒─  #
# ▓▓▓▓▓──────▒▒▒▒▒  #
# ─▓▓▓──▒▒▒▒▒▒▒▒▒─  #
# ──▓▓─▒▒▒▒▒──────  #
# ─────▒▒▒▒▒▒▀▒───  #
# ──────▒▒▒▒▒▒────  #
###################

# Plans:
# get_grade func ⇒ (done)
# new_student func ⇒ (done)
# main_menu func ⇒ (done)
# search_book func ⇒ (done)
# Objects? ⇒ (perhaps)

# Searches the 2D array for a name,
# and returns the information of the
# student once found
def search_book(arr):
  student = input("Enter Student Name: ")
  LB = 0
  UB = (len(arr)-1)

  found = False

  while found == False and LB<=UB:
    MP = (UB + LB) // 2

    if student == arr[MP][0]:
      print("Student Found at Index: ",MP)
      print(arr[MP])
      found = True
        
    elif student < arr[MP][0]:
      UB = (M-1)
        
    elif student > arr[MP][0]:
      LB = (M+1)
        
  if found == False:
    print("Student not recognised.")
      
# Grades:
# A ⇒ 90-100
# B ⇒ 80-89
# C ⇒ 70-79
# D ⇒ 60-69
# E ⇒ 0-59

# Takes the mark entered, and then depending on the
# mark entered, it returns a grade according to the
# boundaries described above

def get_grade(mark):
    if mark >= 0 and mark < 60:
        grade = "E"
    elif mark >= 60 and mark < 70:
        grade = "D"
    elif mark >= 70 and mark < 80:
        grade = "C"
    elif mark >= 80 and mark < 90:
        grade = "B"
    elif mark >= 90 and mark <= 100:
        grade = "A"
    else:
        print("Invalid mark")
        grade = ""
    return grade

def new_student():
    student = []
    name = input("Enter Student name: ")
    mark = int(input("Enter student's mark: "))
    grade = get_grade(mark)
    student.extend([name, mark, grade])
    markbook.append(student)
    markbook.sort(key=lambda x:x[0])

# Defining constant markbook array for later manipulation
markbook = []

# Start of main code (replaced with main_menu function)
# Prints out options and then gets user input
# and then carries out a subroutine depending
# on the user's input
def main_menu():
    complete = False
    while complete == False:
        print("1. Add Student\n2. Search for Student\n3. List all students\n4. Quit")
        choice = int(input("Enter option: "))
        if choice == 1:
            new_student()
        elif choice == 2:
            search_book(markbook)
        elif choice == 3:
            print(*markbook, sep=' | ')
        elif choice == 4:
            complete = True
        else:
            print('Invalid option')

if __name__ == '__main__':
    main_menu()