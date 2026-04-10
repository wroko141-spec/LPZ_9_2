print("=" * 50)
print("ТЕСТИРОВАНИЕ ИМПОРТА ПАКЕТА")
print("=" * 50)

print("\n1. Импорт пакета:")
import mypackage
print(f"   Версия: {mypackage.__version__}")
print(f"   Доступные компоненты: {mypackage.__all__}")

print("\n2. Импорт подпакетов:")
from mypackage import models
from mypackage import utils
from mypackage import api
print("   Подпакеты импортированы успешно")

print("\n3. Импорт классов и функций:")
from mypackage.models import Student, Group
from mypackage.utils import validate_email, format_student_info
from mypackage.api import APIClient

student = Student("Иван", "Петров", 19, "ivan@example.com")
group = Group("ПИН-231")
client = APIClient()

print("   Объекты успешно созданы:")
print(f"   {student}")
print(f"   {group}")
print(f"   APIClient base_url: {client.base_url}")

print("\nВсе импорты работают корректно")