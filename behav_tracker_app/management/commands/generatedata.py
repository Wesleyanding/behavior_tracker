from django.core.management.base import BaseCommand

from behav_tracker_app.models import Teacher

class Command(BaseCommand):
    def handle(self, *args, **kwarg):
        Teacher.objects.filter(is_staff=False).delete()
        for x in range(3):
            teacher = Teacher.objects.create_user(f"testTeacher{x}", '', 'password')
            teacher.name = f'testTeacher{x}'
            teacher.save()
            print(f'created user: testTeacher{x}')