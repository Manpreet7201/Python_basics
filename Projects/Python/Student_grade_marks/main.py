import json

def CalculateGrade(avg):
    if(avg >= 90):
        grade = "A"
    elif(avg >= 75 and avg <= 89):
        grade = "B"
    elif(avg >= 60 and avg <= 74):
        grade = "C"
    elif(avg >= 50 and avg <= 59):
        grade = "D"
    else:
        grade = "F"
    return grade


def add_student():
    sub_dict = {}
    a1 = input("Student name ?")
    
    sub_cn = int(input("How many subject are there ?"))
    mark_ls = []
    for i in range(0, sub_cn):
        mark = int(input("Marks: "))
        mark_ls.append(mark)

    avrg = sum(mark_ls)/len(mark_ls)
    ans = CalculateGrade(avrg)
    
    sub_dict = {
        "name": a1,
        "marks": mark_ls,
        "average": avrg,
        "grade": ans
    }
    return sub_dict

def view_students(students):
    if (len(students) == 0):
        print("No Student Data Available for now.Thanks for visiting us.")
        return
    for el in students:
        print(f"Student name:      {el['name']},")
        print(f"Student average:   {el['average']:.2f},")
        print(f"Student grade:     {el['grade']}")

def save_to_file(students):
    # try:
    with open("my_studens.json", "w") as file:
        # file.write(students)
        json.dump(students, file)
    print(f"Saved {len(students)} student(s) successfully!")
    # except FileExistsError:
    #     print("File does not exists.")

def load_file():
    try:
        with open("my_studens.json", "r") as file:
            # file.read(students)
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("File does not exists.")
        return []

def main():
    students = load_file()
    if len(students) > 0:
        print(f"Loaded {len(students)} student(s) from file.")
    else:
        print("Starting fresh — no saved data found.")
    while True:
        print("\n--- Student Grade Tracker ---")
        print("1. Add student")
        print("2. View all students")
        print("3. Save to file")
        print("4. Exit")
        choice = input("Enter your choice- ")
        if(choice == '1'):
            res = add_student()
            students.append(res)
        elif(choice == '2'):
            view_students(students)
        elif(choice == '3'):
            save_to_file(students)
        elif(choice == '4'):
            print("Thanks for Visiting us.Bye Bye!")
            break
        else:
            print("Invalid option.")
main()


