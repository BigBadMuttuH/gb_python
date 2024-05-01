from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = 'Create user'

    def handle(self, *args, **options):
        # user = User(name='John', email='john@example.com', password='secret', age=25)
        # user = User(name='Alex', email='Alex@example.com', password='1234', age=30)
        user = User(name='Nick', email='Nick@example.com', password='00000', age=45)
        ...
        user.save()
        self.stdout.write(f'User created: {user}')

