# class for students
class StudentForm:
    def __init__(self, Name, Branch, Grades):
        self.Name = Name
        self.Branch = Branch
        self.Grades = Grades


# Karan=StudentForm("Karan","EC",8.39)
# Yash=StudentForm("Yash","Bcom",9.90)
# print("Name : ",Karan.Name,"\nBranch : ",Karan.Branch,"\nGrades : ",Karan.Grades,"\n")
# print("Name : ",Yash.Name,"\nBranch : ",Yash.Branch,"\nGrades : ",Yash.Grades)

# driver code
data = {}
temp = []

while True:
    id = input("Enter the Id: ")
    name = input("Enter the Name: ")
    branch = input("Enter the Branch: ")
    grades = input("Enter the Grades: ")
    user = StudentForm(name, branch, grades)

    temp.append(name)
    temp.append(branch)
    temp.append(grades)

    data[id] = tuple(temp)

    temp.clear()
    print(temp)
    print(data)

    print("Name : ", user.Name, "\nBranch : ", user.Branch, "\nGrades : ", user.Grades)
