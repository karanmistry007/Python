#class to object
print("calss to object:-")
class house:       
    area = "10000sqft"                
    architect = "Karan Mistry"
  
    def display_area(self):
        print("This house is " + self.area)
    def display_architect(self):
        print ("The architect is " + self.architect)
        
        
a = house()                   
print(a.area)                   
a.display_area()                
a.display_architect()     
print("_______________________________________________________")    

#simple inheritance
print("simple inheritance:-")
class parent:                  
    def func1(self):
        print("Parent")
 
class child(parent):    
    def func2(self):           
        print("Child")   
                               
 
test = child()                 
test.func1()                  
test.func2()   
print("_______________________________________________________")    

#multiple inheritance
print("multiple inheritance:-")
class parent1:                     
    def func1(self):                   
        print("Parent1")
 
class parent2:                     
    def func2(self):                   
        print("Parent2")

class parent3:                    
    def func2(self):                    
        print("Parent3")

class child(parent1, parent2,parent3):     
    def func3(self):                     
        print("Child")       
        
                           
test = child()        
test.func1()          
test.func2()     
test.func3()     
print("_______________________________________________________")   

#multilevel inheritance
print("multilevel inheritance:-")
class grandparent:                 
    def func1(self):                   
        print("Grandparent")
 
class parent(grandparent):         
    def func2(self):                   
        print("Parent")
 
class child(parent):               
    def func3(self):                   
        print("Child")   
                               

test = child()                     
test.func1()                       
test.func2()                       
test.func3()          
print("_______________________________________________________")               

#hierachical inheritance
print("hierachical inheritance:-")
class parent:                     
    def func1(self):                   
        print("Parent")
 
class child1(parent):               
    def func2(self):                   
        print("Child1")
 
 
class child2(parent):              
    def func3(self):                   
        print("Child2")   
                               
test1 = child1()                    
test2 = child2() 
 
test1.func1()                      
test1.func2()                      
 
test2.func1()                     
test2.func3() 
print("_______________________________________________________")  


#hybrid inheritance
print("hybrid inheritance:-")
class parent1:                            
    def func1(self):                   
        print("Parent")
 
 
class parent2:                                              
    def func2(self):                   
        print("Parent")
 
class child1(parent1):                      
    def func3(self):                   
        print("Child1")
 
 
class child2(child1, parent2):            
    def func4(self):                   
        print("Child2")   
                               
 

test1 = child1()                          
test2 = child2()
 
test1.func1()                       
test1.func3()                       
 
test2.func1()                       
test2.func2()                      
test2.func3()                       
test2.func4() 