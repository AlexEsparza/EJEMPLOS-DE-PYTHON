import random
# print("Hola mundo")
class User:

    name=None
    email=None

    #metodo de enviar correo
    def send_email(self):
        if self.email is not None:
            print("sending email}:"+self.email)
        else:
            print("error")

    def _str_(self):
        return "User: "+self.name+", "+self.email            
        
    #constructor 
    def _init_(self,name,email):
        self.name=name
        self.email=email

    
       

user1=User("sem","sem.hernandez@utsc.edu.mx")
user1.send_email()
user1.email="sem.hernandez@utsc.edu.mx"
user1.send_email()

class Student(User):
    def _init_(self, name, email, score):
        super()._init_(name, email)
        self.score = score

    def _str_(self):
        return "Student: "+self.name+", "+self.email+", Score: "+str(self.score)    


student1 = Student("estudiante1","est1@utsc.edu.mx",7)
student1.send_email()
print(user1)
print(student1)

list1 = list()
for i in range(10):
    list1.append(Student("Student"+str(i),"email"+str(i)+"@utsc.edu.mx",random.randint(6,10)))

for i in list1:
    print(i)
