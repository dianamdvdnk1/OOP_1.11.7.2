class Human:
    def init(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class Student(Human):
    def init(self, name, surname, age, scholarship: int, elder=False):
        super().init(name, surname, age)
        self.scholarship = scholarship
        self.elder = elder


class Teacher(Human):
    def init(self, name, surname, age, subject, groups: list, salary):
        super().init(name, surname, age)
        self.subject = subject
        self.groups = groups
        self.salary = salary

    def time_machine(self):
        pass


class Group:
    specialtyes = {6: "DevOps", 7: "Prog"}

    def init(self, students: list, name, specialty, courses):
        self.students = students
        self.name = name
        self.__specialty = specialty
        self.courses = courses

    @property
    def name(self):
        return self.__name

    @name.setter
    def setter_name(self, name: str):
        try:
            octets = list(map(int, name.split(".")))
        except Exception:
            raise Exception("Не верное имя группы")

        if len(octets) != 4:
            raise Exception("Не верное имя группы")

        if octets[1] == 9 and not (1 <= octets[0] <= 4):
            raise Exception("Не верное имя группы")
        elif octets[1] == 11 and not (1 <= octets[0] <= 3):
            raise Exception("Не верное имя группы")

        self.__name = name
        self.__setter_specialty(octets[3])

    @property
    def specialty(self):
        return self.__specialty

    def __setter_specialty(self, specialty_num):
        self.__specialty = self.specialtyes[specialty_num]

    def setter_elder(self, student_name, student_surname):

        for student in self.students:
            if student.name == student_name and student_surname == student.surname:
                student.elder = True
                break
        else:
            return None

        for student in self.students:
            if student.elder and student.name != student_name and student_surname != student.surname:
                student.elder = False

    def get_teachers(self):
        return [course.teacher for course in self.courses]

    def get_hours(self):
        return sum([course.hours for course in self.courses])


class Сollege:
    def __init(self, name, groups: list, teachers):
        self.name = name
        self.groups = groups
        self.teachers = teachers


class Subject:
    def init(self, name):
        self.name = name


class Course:
    def init(self, name, hours, teacher, subject: Subject):
        self.name = name
        self.hours = hours
        self.teacher = teacher
        self.subject = subject