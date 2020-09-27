
class Student:
        def _init_(self,age):
                self.age = age
        def getpermit(self):
                
                if self.age <13:
                        raise Exception("you are not eligible")
                else:
                        print("you are eligible to get permit")
        age = int(input('what is your age'))
        student1 = Student(age)
        try:
                student1.getpermit()
        except Exception as e:
                print(f"Error{e}")
                