
from django.urls import path
from . import views
from .views import student_form

urlpatterns = [
    path('', views.index, name="home"),
    path('list/', views.list_stu, name="list"),
    path('student/form/',student_form, name="student_form"),
]
