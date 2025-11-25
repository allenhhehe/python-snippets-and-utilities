class Student:
    def __init__(self,name,score):
      # init method to initialize name and score
       self.name=name       #initialize name    
       self.score=score     #initialize score

    def add_socre(self,points):
        self.score+=points       #method to add points to score

    def is_passed(self):
         return self.score>=60  #method to chekc if student has passed
    
    def __str__(self):
       #print method to display object infromation
        return f"stuendet(name={self.name},score={self.score})"
    
s1=Student("tom",55)
s2=Student("Xie",75)
print(s1)
s1.add_socre(10)
print(s1)
print(s1.is_passed())
student=[s1,s2]
print(student)
