from django.shortcuts import render

def home(request):
    return render(request,'website/home.html')

def about(request):
    return render(request,'website/about.html')

def blog(request):
    return render(request,'website/blog.html')
