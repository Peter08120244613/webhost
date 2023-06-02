

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST['name']
        regn=request.POST['reg']
        email=request.POST['email']
        cla=request.POST['classname']

        obj=Student()
        obj.name=name 
        obj.reg=regn
        obj.email=email
        obj.stuClass=cla
        obj.save()
        return HttpResponse("<h1>Your entry have been saved!</h1>")

    return render(request,'index.html')
def list_stu(request):
    obj =Student.objects.all()
    return render(request,'list.html',{'obj':obj})


from django.shortcuts import render
from .forms import StudentForm

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>'Success!'</h1>")
        else:
            form = StudentForm()
        return render(request, 'student_form.html', {'form':form})
    