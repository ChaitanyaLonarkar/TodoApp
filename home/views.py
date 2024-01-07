
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from home.models import TaskData
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html')

@login_required(login_url='/login')
def home(request):
    # context={'success':False}
    if request.method=='POST':
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        current_user= request.user
        # print(current_user)
        ins=TaskData(TaskTitle=title,TaskDesc=desc,user=current_user)
        ins.save()
        messages.info(request, "Your task is successfully added.")
    return render(request,'home.html')

@login_required(login_url='/login')
def tasks(request):
    allTasks = TaskData.objects.filter(user=request.user).order_by('-id')
    #above line give only data of current user has logged in and task is sorted in desceng order
    # allTasks=TaskData.objects.all().order_by('-id')
    context={'taskss':allTasks}
    return render(request,'tasks.html',context)

@login_required(login_url='/login')
def delete(request,pk):
    delTask=TaskData.objects.get(id=pk)
    delTask.delete()
    return redirect('/tasks')

@login_required(login_url='/login')
def update(request,pk):
    updateTask=TaskData.objects.get(id=pk)
    if request.method=='POST':
        updateTask.TaskTitle=request.POST.get('title')
        updateTask.TaskDesc=request.POST.get('desc')
        updateTask.save()
        return redirect('tasks')
    return render(request,'update.html')

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        #checking that the user having exists in table (
        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Username.")
            return redirect('/login')
        
        # to authenticate username and passward then it create object and check the password is matching or not with the user input
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request, "Invalid Password.")
            return redirect('/login')

        else: 
            login(request,user)
            return redirect('/home')
    return render(request,'login.html')

def register_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')

        # checking if the user is already registerd 
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,"Username is already taken.")
            return redirect('/register')

        user=User.objects.create(first_name=first_name,last_name=last_name,username=username)

        #to make incripted passward otherwise give to above object  as an argument passward=passward
        user.set_password(password) 
        user.save()
        # print(username,password, first_name,last_name)
        messages.add_message(request, messages.INFO, "User Registered Successfully.")
    return render(request,'register.html')
    # return redirect('/login')

@login_required(login_url='/login')
def logout_page(request):
    logout(request)
    return redirect('/login')