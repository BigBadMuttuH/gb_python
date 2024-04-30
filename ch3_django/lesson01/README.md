# Урок 1. Первое приложение 

```bash
pip install django
django-admin.exe startproject myproject
cd myproject
# запуск проекта
python manage.py runserver
# поменять порт сервера
python manage.py runserver 8080
# изменить IP адрес 0.0.0.0:8080 - доступно для всех
python manage.py runserver 0.0.0.0:8080
# добавить разрешенный узлы в settings.py
ALLOWED_HOSTS = [
    '192.168.0.101',
    '127.0.0.1'
]
# создать приложение в проекте (негласное правило - добавлять вконец 'app')
python manage.py startapp myapp
# хорошей привычкой будет добавлять приложение в список INSTALLED_APPS в settings.py
INSTALLED_APPS = [
    ...
    'myapp',
]
# Создание представления в приложении views.py
# настройка urls.py в проекте
from django.urls import path, include

urlpatterns = [
    ...
    path('myapp/', include('myapp.urls')),
]
# настройка urls.py в приложении (нужно создать файл)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
# нужно будет перезапустить сервер
python manage.py startapp myapp
```

# Логирование в Django
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': './log/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'myapp': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```
