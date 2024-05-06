from random import choices

from django.core.management.base import BaseCommand
from myapp3.models import Author, Post

LOREM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
        "Sed euismod, nunc vel tincidunt lacinia, nisl nisl aliquam nisl, eget aliquam nisl nisl sit amet nisl. " \
        "Nunc vel tincidunt lorem, quis bibendum nisl. "


class Command(BaseCommand):
    help = "Generate fake authors and posts"

    def add_arguments(self, parser):
        parser.add_argument(
            'count', type=int, help='Count of users to generate.'
        )

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}', email=f'author{i}@example.com')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title_{j}',
                    content=' '.join(choices(text, k=64)),
                    author=author
                )
                post.save()
