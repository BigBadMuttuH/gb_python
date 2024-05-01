from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = 'Get user by ID'

    def add_arguments(self, parser):
        # использование id не лучший подход, по этому его заменили на pk - primary key
        # parser.add_argument('id', type=int, help='User ID')
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        # user = User.objects.get(id=id)
        # поменяли на filter
        user = User.objects.filter(id=pk).first()
        self.stdout.write(f'User: {user}')

# python.exe .\manage.py get_user 1
# теперь ошибки не будет, если вылезли за границы диапазона id
# ➜ myproject git:(main) ✗ python.exe manage.py get_user 20
# User: None
