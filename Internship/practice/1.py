
class Student:
	
	def __init__(self, name, rollno, percentage):
		self.name = name
		self.rollno = rollno
		self.percentage = percentage


	def accept(self, Name, Rollno, Percentage):
		Name=input("Enter The Name: ")
		Rollno=int(input("Enter RollNo: "))
		Percentage=int(input("Enter Percentage: "))
		ob = Student(Name, Rollno, Percentage) 
		list1.append(ob)


	def display(self, ob):
		print("Name : ", ob.name)
		print("RollNo : ", ob.rollno)
		print("Percentage : ", ob.percentage,"%")
		print("\n")



list1 = []
obj = Student("", 0, 0)

print("\nOperations used, ")
while (1):
	print("\n1.Add Student details\n2.Display Student Details\n3.Exit")
	ch = int(input("Enter choice:"))

	if(ch == 1):
		obj.accept("A", 1, 90)
	elif(ch == 2):
		print("\n")
		print("\nList of Students\n")
		
		for i in range(list1.__len__()):
			obj.display(list1[i])

	elif(ch==3):
		exit(0)
