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
    if request == "POST":
        firstname = request.POST.GET['firstname']
        lastname = request.POST.GET['lastname']
        email = request.POST.GET['emaiil']
        password = request.POST.GET['password']
        password_repeat = request.POST.GET['password_repeat']
        
        user_details = [firstname, lastname, email, password, password_repeat]      
        print(user_details)
    else:
        pass 