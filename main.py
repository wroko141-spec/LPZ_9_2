import json
from mypackage import (
    Student,
    Group,
    APIClient,
    validate_email,
    validate_age,
    format_student_info,
    format_group_report,
    print_colored,
)


def demo_package_usage():
    print_colored("\n" + "=" * 60, "blue")
    print_colored("ДЕМОНСТРАЦИЯ РАБОТЫ ПАКЕТА mypackage", "blue")
    print_colored("=" * 60, "blue")

    print_colored("\n1. СОЗДАНИЕ СТУДЕНТОВ", "yellow")

    students_data = [
        ("Радель", "Закиров", 17, "wroko141@mail.ru"),
        ("Адель", "Миндубаев", 17, "2008adel2008@gmail.com"),
        ("Саня", "Чернов", 17, "chervnov2008@mail.ru"),
        ("Егор", "Ершов", 17, "egorershov0808@mail.ru"),
        ("Андрей", "Погорелов", 17, "Monsu_draiv_gmail.com"),
    ]

    students = []

    for first, last, age, email in students_data:
        valid_email, msg_email = validate_email(email)
        if not valid_email:
            print(f"⚠{msg_email}: {email}")
            email = None

        valid_age, msg_age = validate_age(age)
        if not valid_age:
            print(f"⚠{msg_age} для {first} {last}")
            age = 18

        student = Student(first, last, age, email)
        students.append(student)
        print(f"Создан: {student}")

    print_colored("\n2. ДОБАВЛЕНИЕ ОЦЕНОК", "yellow")

    grades_data = [
        (0, 5, "Осн. Алгоритмов"),
        (0, 4, "Разработка кода"),
        (0, 5, "Базы данных"),
        (1, 5, "Осн. Алгоритмов"),
        (1, 5, "Разработка кода"),
        (1, 4, "Базы данных"),
        (2, 3, "Осн. Алгоритмов"),
        (2, 4, "Разработка кода"),
        (2, 3, "Базы данных"),
        (3, 5, "Осн. Алгоритмов"),
        (3, 5, "Разработка кода"),
        (3, 5, "Базы данных"),
        (4, 4, "Осн. Алгоритмов"),
        (4, 4, "Разработка кода"),
        (4, 5, "Базы данных"),
    ]

    for student_idx, grade, subject in grades_data:
        if student_idx < len(students):
            students[student_idx].add_grade(grade, subject)

    print_colored("\n3. СОЗДАНИЕ ГРУППЫ", "yellow")

    group = Group("ПИН-231", curator="Шишелева Е.А.")
    for student in students:
        group.add_student(student)

    print(format_group_report(group))

    print_colored("\n4. РАБОТА С ВНЕШНИМ API", "yellow")

    client = APIClient()

    print_colored("\nПолучение постов с API...", "blue")
    posts = client.get_posts(5)

    if posts:
        print_colored("\nПоследние посты:", "green")
        for i, post in enumerate(posts, 1):
            print(f"  {i}. {post['title'][:60]}...")
            print(f"     Автор ID: {post['userId']}")
            print()

    print_colored("Получение случайной цитаты...", "blue")
    quote = client.get_random_quote()

    if quote:
        print_colored(f"\n\"{quote['text']}\"", "yellow")
        print_colored(f"  — {quote['author']}\n", "green")

    print_colored("\n5. ФОРМАТИРОВАНИЕ ВЫВОДА", "yellow")

    for student in students[:2]:
        print(format_student_info(student))

    print_colored("\n6. СОХРАНЕНИЕ ДАННЫХ", "yellow")

    group_data = group.to_dict()
    with open("mypackage/data/group_data.json", "w", encoding="utf-8") as f:
        json.dump(group_data, f, ensure_ascii=False, indent=2)

    print_colored(
        "Данные группы сохранены в mypackage/data/group_data.json",
        "green"
    )

    api_stats = client.get_statistics()
    with open("mypackage/data/api_stats.json", "w", encoding="utf-8") as f:
        json.dump(api_stats, f, ensure_ascii=False, indent=2)

    print_colored(
        "Статистика API сохранена в mypackage/data/api_stats.json",
        "green"
    )

    print_colored("\n" + "=" * 60, "blue")
    print_colored("РАБОТА ЗАВЕРШЕНА УСПЕШНО!", "green")
    print_colored("=" * 60, "blue")

    print("\nСтатистика:")
    print(f"  • Всего студентов: {len(students)}")
    print(f"  • Средний балл группы: {group.get_group_average():.2f}")
    print(f"  • Всего API запросов: {api_stats['total_requests']}")
    print(f"  • Базовый URL API: {api_stats['base_url']}")


def interactive_mode():
    print_colored("\n" + "=" * 50, "blue")
    print_colored("ИНТЕРАКТИВНЫЙ РЕЖИМ", "blue")
    print_colored("=" * 50, "blue")

    client = APIClient()

    while True:
        print("\nВыберите действие:")
        print("1. Получить посты")
        print("2. Получить пользователей")
        print("3. Получить случайную цитату")
        print("4. Показать статистику запросов")
        print("0. Выход")

        choice = input("\nВаш выбор: ").strip()

        if choice == "0":
            print_colored("До свидания!", "green")
            break

        if choice == "1":
            try:
                limit = int(input("Количество постов (по умолчанию 5): ") or "5")
                posts = client.get_posts(limit)
                if posts:
                    print_colored(f"\n--- ПОСТЫ ({len(posts)}) ---", "yellow")
                    for post in posts:
                        print(f"\n{post['title']}")
                        print(f"   {post['body'][:100]}...")
            except ValueError:
                print("Некорректный ввод")

        elif choice == "2":
            users = client.get_users()
            if users:
                print_colored(f"\n--- ПОЛЬЗОВАТЕЛИ ({len(users)}) ---", "yellow")
                for user in users:
                    print(f"\n{user['name']}")
                    print(f"  {user['email']}")
                    print(f"  {user['address']['city']}")

        elif choice == "3":
            quote = client.get_random_quote()
            if quote:
                print_colored(f"\n\"{quote['text']}\"", "yellow")
                print_colored(f"  — {quote['author']}\n", "green")

        elif choice == "4":
            stats = client.get_statistics()
            print_colored("\n--- СТАТИСТИКА ---", "yellow")
            for key, value in stats.items():
                print(f"  {key}: {value}")

        else:
            print("Неверный выбор. Попробуйте снова.")


def main():
    print("""
ЛАБОРАТОРНАЯ РАБОТА: СОЗДАНИЕ ПАКЕТА И РАБОТА С API
Выполнили: Закиров Радель, Миндубаев Адель
""")

    while True:
        print("\nВыберите режим работы:")
        print("1. Демонстрация пакета")
        print("2. Интерактивный режим")
        print("0. Выход")

        choice = input("\nВаш выбор: ").strip()

        if choice == "0":
            print("До свидания!")
            break
        elif choice == "1":
            demo_package_usage()
        elif choice == "2":
            interactive_mode()
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()