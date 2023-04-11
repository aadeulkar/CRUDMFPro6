from django.shortcuts import render, redirect
from .forms import StudentForm
from.models import Student
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_url')
def addstudentView(request):
    form = StudentForm()
    template_name = 'CRUD_APP/add.html'
    context = {'form': form}
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showstudent_url')
    return render(request, template_name, context)

@login_required(login_url='login_url')
def showstudentView(request):
    stu = Student.objects.all()
    template_name= 'CRUD_APP/show.html'
    context = {'stu': stu}
    return render(request, template_name, context)


def updatestudentView(request, pk):
    stu = Student.objects.get(id=pk)
    form = StudentForm(instance= stu)
    template_name= 'CRUD_APP/add.html'
    context ={'form':form}
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=stu)
        if form.is_valid():
            form.save()
            return redirect('showstudent_url')
    return render(request, template_name, context)


def deletestudentView(request, pk):
    stu = Student.objects.get(id=pk)
    template_name= 'CRUD_APP/deletecnf.html'
    context= {'stu': stu}
    if request.method == 'POST':
        stu.delete()
        return redirect('showstudent_url')
    return render(request, template_name, context)

# Create your views here.
