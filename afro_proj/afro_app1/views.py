from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    p_title = "AFRO DJANGO TEMPLATING"
    user_name = "Brian Abura"
    gender = "Male"
    return render(request, 'index.html', {'p_title': p_title, 'user_name':user_name, 'gender': gender})

def register(request):
    return render(request, 'register.html')

def registration(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    password_repeat = request.POST['password_repeat']
    
    user_details = [firstname, lastname, email, password, password_repeat]      
    return render(request, 'index.html', {'user_details': user_details})