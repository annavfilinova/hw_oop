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


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

# Добавим курсы и оценки для тестирования
student.courses_in_progress = ['Python', 'Git']
student.finished_courses = ['Введение в программирование']
student.grades = {
    'Python': [10, 9, 8],
    'Git': [9, 9]
}

lecturer.courses_attached = ['Python', 'Git']
lecturer.grades = {
    'Python': [10, 9],
    'Git': [8, 7]
}

# Вывод информации о проверяющем
print(reviewer)  # Вывод информации о проверяющем

# Вывод информации о лекторе
print(lecturer)  # Вывод информации о лекторе

# Вывод информации о студенте
print(student)   # Вывод информации о студенте




