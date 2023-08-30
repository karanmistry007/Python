 #Constructor
class Family:  
    members=5
    def __init__(self, count):  
        print("This is parametrized constructor")  
        self.members = count
    def show(self):  
        print("No. of members is", self.members)  
        
object = Family(10)  
object.show()  