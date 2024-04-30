from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def people(request):
    return render(request,'people.html')

def product(request):
    return render(request,'product.html')