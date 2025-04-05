from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')
def proj1(request):
    return render(request,'proj1.html')
def projects(request):
    return render(request,'projects.html')
def singlepost(request):
    return render(request,'singlepost.html')



# Create your views here.
