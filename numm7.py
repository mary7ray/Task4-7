class Student:

    def __init__(self, name,age,major):
        self.name = name
        self.age = age
        self.major = major


    def output(self):
        return "name: ",self.name, "age: ",str(self.age),"major: ",self.major

St1 = Student("Frank Iero",23,"Music").output()
St2 = Student("Gerard Way",24,"Art").output()
St3 = Student("Gared Leto",22,"Cinema-Movie").output()

print(" ".join(St1))
print(" ".join(St2))
print(" ".join(St3))