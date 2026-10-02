class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def show_info(self):
        return f"{self.name} {self.surname}, вік: {self.age}"


class Student(Person):
    def __init__(self, name, surname, age, group):
        super().__init__(name, surname, age)
        self.group = group

    def show_info(self):
        return f"Студент: {self.name} {self.surname}, вік: {self.age}, група: {self.group}"


class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, surname):
        for student in self.students:
            if student.surname == surname:
                return student
        return None

    def remove_student(self, surname):
        student = self.find_student(surname)

        if student is not None:
            self.students.remove(student)

    def __str__(self):
        result = ""

        for student in self.students:
            result += student.show_info() + "\n"

        return result



student1 = Student("Максим", "Петренко", 16, "КБ-11")
student2 = Student("Олексій", "Іваненко", 17, "КБ-11")
student3 = Student("Анна", "Коваленко", 16, "КБ-11")


group = Group()


group.add_student(student1)
group.add_student(student2)
group.add_student(student3)


print("Студенти групи:")
print(group)


student = group.find_student("Іваненко")

if student:
    print("Знайдений студент:")
    print(student.show_info())
else:
    print("Студента не знайдено")


group.remove_student("Іваненко")

print("\nПісля видалення:")
print(group)