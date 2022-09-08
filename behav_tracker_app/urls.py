from django.urls import path
from . import views

app_name = 'behavtrackerapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('api/teachers', views.get_teachers, name='get_teachers')
]
