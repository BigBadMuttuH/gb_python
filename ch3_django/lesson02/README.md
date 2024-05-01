# Урок 2. Модели

## Поддержка изображений
```powershell
# установить для работы с изображениями
python -m pip install Pillow
```
## Миграции
```powershell
# создание миграции
python.exe .\manage.py makemigrations myapp2
# применение миграции
python.exe .\manage.py migrate
```
## Добавление своих команд в manage.py
Нужно добавить следующую иерархию файлов
```cmd
├───myapp2
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───management
│   │   │   __init__.py
│   │   │
│   │   └───commands
│   │           my_command.py
│   │           __init__.py


# запустить комманду
python.exe .\manage.py my_command -h
```

```python
# my_command.py
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'My command'

    def handle(self, *args, **kwargs):
        self.stdout.write('My command')
```