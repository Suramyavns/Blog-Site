from django.shortcuts import render,redirect
from django.db.models import Q
from .models import blog,topic,User
from .forms import blogform,topicform
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    return render(request,'index.html')

def bloglist(request):
    if request.GET.get('q')!=None:
        topicname = request.GET.get('q')
    else:
        topicname = ''

    blogs = blog.objects.all().filter(
        Q(topicname__topicname__icontains=topicname) |
        Q(title__icontains = topicname) |
        Q(body__icontains=topicname)
        )
    num_blogs = blogs.count()
    topics = topic.objects.all()
    return render(request, 'bloglist.html', {'blogs':blogs,'topics':topics,'num_blogs':num_blogs})

def blogpage(request,slug):
    blogpost = blog.objects.get(slug=slug)
    return render(request, 'blogpage.html', {'blogpost':blogpost})

def createblog(request):
    if request.method == 'POST':
        blog = blogform(request.POST)
        if blog.is_valid():
            obj = blog.save(commit=False)
            obj.slug = blog.data['title'].replace(' ','-')
            obj.save()
            return redirect('index')
    return render(request,'addblog.html',{'form':blogform})

def updateblog(request, id):
    blogpost = blog.objects.get(id=id)
    form = blogform(instance=blogpost)
    if(request.method=='POST'):
        newform = blogform(request.POST, instance=blogpost)
        if newform.is_valid():
            newform.save()
            return redirect('blogs')
    return render(request,'updateblog.html',{'form':form})

def deleteblog(request,id):
    blogpost = blog.objects.get(id=id)
    if request.method=='POST':
        blogpost.delete()
        return redirect('blogs')
    return render(request,'delete.html',{'obj':blogpost})

def loginpage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User not found!')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user=user)
            return redirect('index')
        else:
            messages.error(request,"Username/Password is wrong!")
    return render(request,'login_register.html')

def logoutuser(request):
    logout(request)
    return redirect('index')

def addtopic(request):
    if request.method=='POST':
        topic = topicform(request.POST)
        if topic.is_valid():
            topic.save()
            return redirect('index')
    return render(request,'addtopic.html',{'topicform':topicform})
