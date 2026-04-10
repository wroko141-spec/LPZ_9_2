def format_student_info(student):
    separator = "=" * 50
    return f"""
{separator}
СТУДЕНТ: {student.get_full_name()}
{separator}
ID студента: {student.student_id}
Возраст: {student.age}
Email: {student.email if student.email else 'Не указан'}
Средний балл: {student.get_average_grade():.2f}
Количество оценок: {len(student.grades)}
Дата создания: {student.created_at.strftime('%d.%m.%Y %H:%M')}
{separator}
"""


def format_grades(student, show_all=False):
    if not student.grades:
        return "Оценок пока нет"

    if show_all:
        result = f"Оценки студента {student.get_full_name()}:\n"
        for i, grade_info in enumerate(student.grades, 1):
            date_str = grade_info["date"].strftime("%d.%m")
            result += (
                f"  {i}. {grade_info['subject']}: "
                f"{grade_info['grade']} ({date_str})\n"
            )
        return result

    return (
        f"Средний балл {student.get_full_name()}: "
        f"{student.get_average_grade():.2f}"
    )


def format_group_report(group):
    separator = "=" * 60

    report = f"""
{separator}
ОТЧЕТ ПО ГРУППЕ: {group.name}
{separator}
Куратор: {group.curator if group.curator else 'Не назначен'}
Количество студентов: {group.get_students_count()}
Средний балл группы: {group.get_group_average():.2f}
"""

    best = group.get_best_student()
    if best:
        report += (
            f"Лучший студент: {best.get_full_name()} "
            f"(ср. балл: {best.get_average_grade():.2f})\n"
        )

    report += "\nСПИСОК СТУДЕНТОВ:\n"
    report += "-" * 60 + "\n"

    for i, student in enumerate(group.students, 1):
        report += (
            f"{i:2}. {student.get_full_name():20} | "
            f"ID: {student.student_id} | "
            f"Ср.балл: {student.get_average_grade():.2f}\n"
        )

    report += separator
    return report


def print_colored(text, color="green"):
    colors = {
        "green": "\033[92m",
        "red": "\033[91m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "reset": "\033[0m",
    }

    print(f"{colors.get(color, colors['reset'])}{text}{colors['reset']}")