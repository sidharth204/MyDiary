from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Create the MyDiary admin user"

    def handle(self, *args, **options):

        username = "admin"
        email = "ksidharth965@gmail.com"
        password = "Pass123"

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(
                    f"User '{username}' already exists."
                )
            )
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Admin user created successfully!"
            )
        )