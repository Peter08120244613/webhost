from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'


from django import forms

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()

