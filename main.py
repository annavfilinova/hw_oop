#Задание 1
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    #Задание 2. Выставление оценок лекторам
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def get_average_grade(self):
        if self.grades:
            return sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values())
        return 0
    
    #Сравнение студента и лектора по средней оценке
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() < other.get_average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() <= other.get_average_grade()
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() > other.get_average_grade()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() >= other.get_average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() == other.get_average_grade()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() != other.get_average_grade()
        return NotImplemented

        
    def __str__(self):
        avg_grade = self.get_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress else 'Нет'
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else 'Нет'
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")


      
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
   

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {} #Словарь для хранения оценок по курсам
    
    def get_average_grade(self):
        if self.grades:
            return sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values())
        return 0

    def __str__(self):
        avg_grade = self.get_average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade}")
    
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() < other.get_average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() <= other.get_average_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() > other.get_average_grade()
        return NotImplemented
    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() >= other.get_average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() == other.get_average_grade()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() != other.get_average_grade()
        return NotImplemented

    

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
    
    #выставлять оценки за дз 
    def rate_lecture(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Пример использования
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Сергей', 'Сергеев')

reviewer = Reviewer('Пётр', 'Петров')
student1 = Student('Алёхина', 'Ольга', 'Ж')
student2 = Student('Дмитрий', 'Дмитриев', 'М')

# Добавили курсы и оценки для тестирования
student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']
student1.grades = {'Python': [10, 9, 8], 'Git': [9, 9]}

student2.courses_in_progress = ['Python', 'Java']
student2.finished_courses = ['Введение в программирование']
student2.grades = {'Python': [9, 8], 'Java': [10, 9]}

lecturer1.courses_attached = ['Python']
lecturer1.grades = {'Python': [10, 9]}

lecturer2.courses_attached = ['Python']
lecturer2.grades = {'Python': [8, 7]}

# Сравнение студентов
print(student1 > student2)  # Вывод: True (если student1 имеет более высокую среднюю оценку)
print(student1 < student2)  # Вывод: False

# Сравнение лекторов
print(lecturer1 > lecturer2)  # Вывод: True (если lecturer1 имеет более высокую среднюю оценку)
print(lecturer1 < lecturer2)  # Вывод: False