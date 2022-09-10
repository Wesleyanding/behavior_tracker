from django.urls import path
from . import views

app_name = 'behavtrackerapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('teachers/', views.get_teachers, name='get_teachers'),
    path('student/<str:student_id>/', views.get_student, name='get_student')
]
