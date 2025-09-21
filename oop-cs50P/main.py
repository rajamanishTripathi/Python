# def main():
#     name,house = get_student()
#     print(f"{name} from {house}")


# def get_student():
#     name = input("Name : ")
#     house = input("House: ")
#     return name,house


# if __name__ == "__main__":
#     main()



# ----------------------Tuple----------------
# Tuple -- immutable
# def main():
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")


# def get_student():
#     name = input("Name : ")
#     house = input("House: ")
#     return (name,house)


# if __name__ == "__main__":
#     main()



# ----------------------List----------------
# List -- mutable
# def main():
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")


# def get_student():
#     name = input("Name : ")
#     house = input("House: ")
#     return [name,house]


# if __name__ == "__main__":
#     main()

# ----------------------Dictionaries----------------
# Dict -- mutable
# def main():
#     student = get_student()
#     if student["name"] == "Padma":
#         student["house"] = "wee"
#     print(f"{student['name']} from {student['house']}")


# def get_student():
#     student = {}
#     student["name"] = input("Name : ")
#     student["house"] = input("House: ")
#     return student

# OR

# def get_student():
#     name = input("Name : ")
#     house = input("House: ")
#     return {"name": name, "house": house}


# if __name__ == "__main__":
#     main()

# ----------------------class 1 ----------------

# class Student:
#     pass

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")


# def get_student():
#     student = Student()
#     student.name = input("Name : ")
#     student.house = input("House: ")
#     return student


# if __name__ == "__main__":
#     main()


# ----------------------class 2 ----------------

# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing Name")
#         if house not in ["ww","ee"]:
#             raise ValueError("Invalid House")
#         self.name = name
#         self.house = house
        

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")


# def get_student():
#     name = input("Name : ")
#     house = input("House: ")
#     return Student(name,house)


# if __name__ == "__main__":
#     main()


# ----------------------class 3 ----------------

# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing Name")
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"
    
#     # Getter
#     @property
#     def house(self):
#         return self._house
    
#     #Setter
#     @house.setter
#     def house(self,house):
#         if house not in ["ww","ee"]:
#             raise ValueError("Invalid House")
#         self._house = house

        

# def main():
#     student = get_student()
#     # student.house = "house"
#     print(student)


# def get_student():
#     name = input("Name : ")
#     house = input("House: ")
#     return Student(name,house)


# if __name__ == "__main__":
#     main()



# class methods vs instance methods
import random

# class Hat:
#     def __init__(self):
#         self.house = ["Delhi","Pune","Hyderabad"]

#     def sort(self,name):
#         print(name, "is in",random.choice(self.house))
    


# hat = Hat()
# hat.sort("Rajkar")




# class methods vs instance methods

class Hat:
    house = ["Delhi","Pune","Hyderabad"]


    @classmethod
    def sort(cls,name):
        print(name, "is in",random.choice(cls.house))
    


Hat.sort("Rajkar")