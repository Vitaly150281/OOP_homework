class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in self.courses_in_progress and course in lectur.courses_attached:
            if course in lectur.grades:
                lectur.grades[course] += [grade]
            else:
                lectur.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average(self):
        _count = 0
        _sum = 0
        for key in self.grades:
            _count += len(self.grades[key])
            _sum += sum(self.grades[key])
        if _count > 0:
            av = round(_sum/_count, 1)
            return av
        else:
            return 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.__average() < other.__average()

    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {self.__average()}\n " \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n Завершенные курсы: {', '.join(self.finished_courses)}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __average(self):
        _count = 0
        _sum = 0
        for key in self.grades:
            _count += len(self.grades[key])
            _sum += sum(self.grades[key])
        if _count > 0:
            av = round(_sum/_count, 1)
            return av
        else:
            return 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lectur!')
            return
        return self.__average() < other.__average()

    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.__average()}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f' Имя: {self.name}\n Фамилия: {self.surname}'


Student_1 = Student('Ivan', 'Ivanov', 'm')
Student_1.finished_courses = ['history', 'philosophy']
Student_1.grades['history'] = [10, 10, 10, 10]
Student_1.grades['philosophy'] = [9, 8, 8, 7]
Student_1.courses_in_progress = ['politics']
Student_1.grades['politics'] = [10, 8]

Student_2 = Student('Vera', 'Titova', 'w')
Student_2.finished_courses = ['history']
Student_2.grades['history'] = [9, 9, 9, 9]
Student_2.courses_in_progress = ['philosophy', 'politics']
Student_2.grades['philosophy'] = [9, 8, 9]
Student_2.grades['politics'] = [10, 8]

Lectur_1 = Lecturer('Petr', 'Petrov')
Lectur_1.courses_attached = ['history', 'politics']
Lectur_1.grades = {'history': [10, 10, 9, 5, 6, 7],
                   'politics': [8, 5, 9, 8]}

Lectur_2 = Lecturer('Marina', 'Berkova')
Lectur_2.courses_attached = ['philosophy']
Lectur_2.grades = {'philosophy': [10, 10, 10, 10, 10, 10]}

Reviewer_1 = Reviewer('Alla', 'Borisova')
Reviewer_1.courses_attached = ['philosophy']

Reviewer_2 = Reviewer('Fedor', 'Fedorov')
Reviewer_2.courses_attached = ['history', 'politics']

Student_1.rate_lecturer(Lectur_1, 'politics', 9)
Reviewer_2.rate_hw(Student_1, 'politics', 9)

print(Lectur_1)
print(Lectur_2)
print(Lectur_1 < Lectur_2)


def student_average(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
        if course_name in stud.courses_in_progress or course_name in stud.finished_courses:
            for grade in stud.grades[course_name]:
                sum_all += grade
                count_all += 1
    average_all = round(sum_all / count_all, 1)
    return average_all

def lectur_average(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if course_name in lect.courses_attached:
            for grade in lect.grades[course_name]:
                sum_all += grade
                count_all += 1
    average_all = round(sum_all / count_all, 1)
    return average_all

student_list = [Student_1, Student_2]
lecturer_list = [Lectur_1, Lectur_2]
course = 'history'

print(f"Средняя оценка всех студентов курса {course}: {student_average(student_list, course)}")
print(f"Средняя оценка лекторов курса {course}: {lectur_average(lecturer_list, course)}")