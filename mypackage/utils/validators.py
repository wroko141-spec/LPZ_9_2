import re


def validate_email(email):
    if not email:
        return False, "Email не может быть пустым"

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(pattern, email):
        return True, "Email корректен"
    return False, "Некорректный формат email"


def validate_age(age):
    if not isinstance(age, (int, float)):
        return False, "Возраст должен быть числом"

    if age < 16:
        return False, "Студент должен быть старше 16 лет"

    if age > 100:
        return False, "Некорректный возраст"

    return True, "Возраст корректен"


def validate_grade(grade):
    if not isinstance(grade, (int, float)):
        return False, "Оценка должна быть числом"

    if grade < 2 or grade > 5:
        return False, "Оценка должна быть от 2 до 5"

    return True, "Оценка корректна"


def validate_name(name):
    if not name or not isinstance(name, str):
        return False, "Имя не может быть пустым"

    if len(name) < 2:
        return False, "Имя должно содержать минимум 2 символа"

    cleaned = name.replace("-", "").replace(" ", "")
    if not cleaned.isalpha():
        return False, "Имя должно содержать только буквы"

    return True, "Имя корректно"


if __name__ == "__main__":
    test_emails = ["wroko141@mail.ru", "nevern_email", "student@domen", "a@b.c"]
    for email in test_emails:
        valid, msg = validate_email(email)
        print(f"{email}: {msg}")