class student:
    name = ''
    group = ''
    age = 0
    grades = []
    gpa = 0
    def __init__(self, name, group='', age=0, grades=()):
        self.name = name
        self.group = group
        self.age = age
        self.grades = grades
        if grades:
            self.gpa = round(sum(grades) // len(grades), 2)
    def show_info(self):
        print(f'{self.name} ({self.age} років), група {self.group} ')
        print(f'Середній бал: {self.gpa} ({self.grades})')

student1 = student(name = "Andriy", group = "B2121", age = 11, grades = [12, 11, 11, 12, 10, 12, 10])
student2 = student(name = "Kiril", group = "B2121", age = 12, grades = [2, 1, 6, 3, 4, 5, 12])
student3 = student(name = "Edison", group = "B2121", age = 12, grades = [8, 9, 6, 7, 8, 7, 10])

student1.show_info()
student2.show_info()
student3.show_info()