class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            lecturer.grades += [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Math']
best_student.finished_courses += ['Git']

middle_student = Student('Abigail', 'Gibson', 'female')
middle_student.courses_in_progress += ['Python']
middle_student.courses_in_progress += ['Git']
middle_student.finished_courses += ['Math']

worst_student = Student('Mark', 'Goodman', 'male')
worst_student.courses_in_progress += ['Python']
worst_student.courses_in_progress += ['Git']
worst_student.courses_in_progress += ['Math']

python_reviewer = Reviewer('Some', 'Buddy')
python_reviewer.courses_attached += ['Python']
python_reviewer.rate_hw(best_student, 'Python', 10)

git_reviewer = Reviewer('Ronald', 'Barker')
git_reviewer.courses_attached += ['Git']
git_reviewer.rate_hw(middle_student, 'Git', 7)

math_reviewer = Reviewer('Jacob', 'Cooper')
math_reviewer.courses_attached += ['Math']
math_reviewer.rate_hw(worst_student, 'Math', 9)

python_lecturer = Lecturer('Tyler', 'Atkinson')
python_lecturer.courses_attached += ['Python']

git_lecturer = Lecturer('Dylan', 'Dennis')
git_lecturer.courses_attached += ['Git']

math_lecturer = Lecturer('Noel', 'Dean')
math_lecturer.courses_attached += ['Math']

best_student.rate_hw(python_lecturer, 'Python', 10)
middle_student.rate_hw(python_lecturer, 'Python', 6)
worst_student.rate_hw(python_lecturer, 'Python', 4)

middle_student.rate_hw(git_lecturer, 'Git', 5)
worst_student.rate_hw(git_lecturer, 'Git', 2)

best_student.rate_hw(math_lecturer, 'Math', 9)
worst_student.rate_hw(math_lecturer, 'Math', 3)

print(f'Оценки полученные python_lecturer от студентов: {python_lecturer.grades}')
print(f'Оценки полученные git_lecturer: {git_lecturer.grades}')
print(f'Оценки полученные math_lecturer: {math_lecturer.grades}')

print(f'Оценка полученная студентом best_student от python_reviewer: {best_student.grades}') #{Key = предмет : value = оценка}
#
print(f'Оценка полученная студентом middle_student от git_reviewer: {middle_student.grades}')
print(f'Оценка полученная студентом worst_student от math_reviewer: {worst_student.grades}')
