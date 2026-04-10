from datetime import datetime
from mypackage.models.student import Student


class Group:
    def __init__(self, name, curator=None):
        self.name = name
        self.curator = curator
        self.students = []
        self.created_at = datetime.now()

    def add_student(self, student):
        if not isinstance(student, Student):
            print("Ошибка: можно добавлять только объекты Student")
            return False

        self.students.append(student)
        print(f"Студент {student.get_full_name()} добавлен в группу {self.name}")
        return True

    def remove_student(self, student_id):
        for i, student in enumerate(self.students):
            if student.student_id == student_id:
                removed = self.students.pop(i)
                print(f"Студент {removed.get_full_name()} удален из группы {self.name}")
                return removed

        print(f"Студент с ID {student_id} не найден")
        return None

    def get_group_average(self):
        if not self.students:
            return 0
        total = sum(student.get_average_grade() for student in self.students)
        return total / len(self.students)

    def get_best_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.get_average_grade())

    def get_students_count(self):
        return len(self.students)

    def to_dict(self):
        return {
            "name": self.name,
            "curator": self.curator,
            "students_count": self.get_students_count(),
            "average_grade": self.get_group_average(),
            "students": [student.to_dict() for student in self.students],
            "created_at": self.created_at.isoformat(),
        }

    def __str__(self):
        return f"Group: {self.name} (студентов: {len(self.students)})"