from django.core.management.base import BaseCommand
from myapp2.models import Author, Post


class Command(BaseCommand):
    help = 'Generate fake data'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of users to generate')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(1, count + 1):
            author = Author(name=f'Name{i}', email=f'email{i}@example.com')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title #{j}',
                    content=f'Text from {author.name} #{j} is a bla bla meny long text',
                    author=author
                )
                post.save()
