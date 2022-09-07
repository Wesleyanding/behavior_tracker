from django.core.management.base import BaseCommand
import random
from behav_tracker_app.models import Teacher, Student, Class, Behavior

class Command(BaseCommand):
    def handle(self, *args, **kwarg):
        Teacher.objects.filter(is_staff=False).delete()
        Student.objects.all().delete()
        Class.objects.all().delete()
        Behavior.objects.all().delete()

        cls = []
        for x in range (3):
            cl = Class()
            cl.name = f'testClass{x}'
            cl.save()
            cls.append(cl)

        behaviors = []
        for x in range(10):
            behavior = Behavior()
            behavior.antecedent = f"testAntecedent{x}"
            behavior.behavior = f'testBehavior{x}'
            behavior.intervention = f'testIntervention{x}'
            behavior.location = f'testLocation{x}'
            behavior.save()
            behaviors.append(behavior)

        students = []
        for x in range(30):
            student = Student()
            student.name = f'testStudent{x}'
            student.grade = '2nd'
            student.save()
            
            #TODO add class to students
            class_to_add = random.choices(cls, k=random.randint(1, 3))
            for cl in cls:
                student.classes.add(cl)
            #TODO add behaviors to students
            behav_to_add = random.choices(behaviors, k=random.randint(1, 10))
            for behavior in behaviors:
                student.behavior.add(behavior)
            student.save()
            students.append(student)
            
        for x in range(3):
            teacher = Teacher.objects.create_user(f"testTeacher{x}", '', 'password')
            teacher.name = f'testTeacher{x}'
            print(f'created user: testTeacher{x}')

            #TODO add student to teacher
            students_to_add = random.choices(students, k=random.randint(1, 31))
            for student in students:
                teacher.student.add(student)
            
            classes_to_add = random.choices(cls, k=random.randint(1, 3))
            for cl in cls:
                teacher.classes.add(cl)
            teacher.save()




        