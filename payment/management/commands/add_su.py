from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            username='admin',
            email='admin@test.com',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        user.set_password('12345')
        user.save()
