from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request, 'about.html')
def home(request):
    return render(request,'home.html')