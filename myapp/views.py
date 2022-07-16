from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Blog
from .forms import edit_blog
# Create your views here.

def home(request):
    myblog=Blog.objects.all()
    print(myblog)
    return render(request, 'home.html', {'mblog':myblog})

def blog_post(request):
    if request.method=='POST':
        utitle=request.POST.get('title')
        udesc=request.POST.get('desc')
        # print(utitle, udesc)
        blogdata=Blog(title=utitle, desc=udesc, user_id=request.user)
        blogdata.save()
        messages.success(request, 'Post has been submitted Successfully!!')
        return redirect('home')
    return render(request, 'blogpost.html')

def blog_detail(request, id):
    mblog=Blog.objects.get(id=id)
    return render(request, 'blogdetail.html', {'iblog':mblog})

def edit(request, id):
    ublog=Blog.objects.get(id=id)
    editblog=edit_blog(instance=ublog)
    if request.method=='POST':
        editform=edit_blog(request.POST, instance=ublog)
        if editform.is_valid():
            editform.save()
            messages.success(request, 'Post has been Updated')
            return redirect('/')
    return render(request, 'edit.html', {'uedit':editblog})


def delete(request, id):
    mblog=Blog.objects.get(id=id)
    mblog.delete()
    messages.success(request, 'Post has been Deleted')
    return redirect('/')

def u_login(request):
    if request.method=="POST":
        Uname = request.POST.get('uname')
        Upass = request.POST.get('upass1')
        myuser=authenticate(request, username=Uname, password=Upass)
        if myuser is not None:
            login(request, myuser)
            return redirect('/')
        else:
            messages.warning(request, 'Invalid Credential!')
            return redirect('ulogin')
    return render(request, 'login.html')

def register(request):
    if request.method=="POST":
        f_name = request.POST.get('fname')
        l_name = request.POST.get('lname')
        u_name = request.POST.get('uname')
        u_email = request.POST.get('uemail')
        u_pass1 = request.POST.get('upass1')
        u_pass2 = request.POST.get('upass2')
        if u_pass1!=u_pass2:
            messages.warning(request, 'Password does not match')
            return redirect('uregister')
        elif User.objects.filter(username=u_name).exists():
            messages.warning(request, 'username alredy taken')
            return redirect('uregister')
        
        elif User.objects.filter(email=u_email).exists():
            # messages.warning(request, 'Email alredy taken')
            return redirect('uregister')
        else:
            # print(f_name, l_name, u_name, u_email, u_pass1, u_pass2 )
            cuser=User.objects.create_user(first_name=f_name, last_name=l_name, username=u_name, email=u_email, password=u_pass1)
            cuser.save()
            messages.success(request, 'User has been Registerd Successfully!!')
            return redirect('ulogin')
    return render(request, 'register.html')

def u_logout(request):
    logout(request)
    return redirect('/')

