from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from .models import *
from django.db.models import Q
import re

def Home(request):
    student = Student.objects.all()
    context = {
        'student' :  student 
    }
    return render(request, 'home.html', context)

def Add_Student(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        if Student.objects.filter(email=email).exists():
            return HttpResponse("<h1> Email already exists use another email </h1>")
        else:
            student = Student(
                name = name,
                email  = email
        )
        student.save()
        return redirect('home')
    return render(request, 'add.html')

def Update_Student(request, id):
    stu = get_object_or_404(Student, id=id)
    if request.method=="POST":
        stu.name = request.POST.get('name')
        stu.email = request.POST.get('email')
        stu.save()
        return redirect('home')
    return render(request, 'update.html', {'student': stu})

def Delete_Student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('home')

def Search(request):
    search = request.GET.get('search')
    if search:
        results = Student.objects.filter(
            Q(name__icontains=search) | Q(email__icontains=search)
        )
    else:
        results = Student.objects.all()
    
    if not results.exists():
        return HttpResponse("<h1> Data No Match <h1>")

    context = {
        'results': results,
    }
    return render(request, 'search.html', context)
# def Search(request):
#     query_student=request.GET['query']
#     student= Student.objects.filter(name_icontains=query_student) | Student.objects.filter(student_class_icontains=query_student)
#     return render(request, 'show_student.html', {'student': student, 'query_student':query_student})

def Login(request):
    if request.method=="POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        user1 = authenticate(request, username=name, password=password)
        if user1 is not None:
            auth_login(request, user1)
            return redirect("home")
        else:
            return HttpResponse("<h1> Password Is Incorrect Please Try Again</h1>")

    return render(request, 'login.html')

def Signup(request):
    if request.method=="POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        pas = request.POST.get("password")
        cpas = request.POST.get("cpassword")
        if pas != cpas:
            return HttpResponse("<h1> Password Not Match Please Try Again </h1>")
        else:
            sin = User.objects.create_user(
                username = name,
                email = email,
                password = pas
            )
            sin.save()
            return redirect('login')
    return render(request, 'signup.html')






# Create your views here.
