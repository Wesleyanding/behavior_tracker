from django.urls import path
from . import views

app_name = 'behavtrackerapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('viewstudents/', views.students, name='viewstudents'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('teachers/', views.get_teachers, name='get_teachers'),
    path('student/<str:student_id>/', views.get_student, name='get_student'),
    path('viewStudents/', views.view_students, name='viewStudents'),
    path('save_behav/<str:student_id>', views.save_behav, name="save_behav"),
    path('studentinfo/<str:student_id>', views.student_info, name="student_info"),
    
]
