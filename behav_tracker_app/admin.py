from django.contrib import admin
from .models import Behavior, Class, Student, Teacher

admin.site.register(Behavior)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Teacher)