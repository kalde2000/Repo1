from django.core.management.base import BaseCommand
from ...models import User, Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            for i in range(1,4):
                user = User.objects.create_user(
                    username=f'user000{i}',
                    password=f'user000{i}user000{i}')
                user.save()
            c01 = Category.objects.create(name = 'c01',
                                          description = 'c01')
            c01.save()
            c01_01 = Category.objects.create(name = 'c01_01',
                                             description = 'c01_01',
                                             parent = c01)
            c01_01.save()
            c01_01_01 = Category.objects.create(name = 'c01_01_01',
                                                description = 'c01_01_01',
                                                parent = c01_01)
            c01_01_01.save()
            c01_01_02 = Category.objects.create(name = 'c01_01_02',
                                                description = 'c01_01_02',
                                                parent = c01_01)
            c01_01_02.save()
        except Exception:
            pass
