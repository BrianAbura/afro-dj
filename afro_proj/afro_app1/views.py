from django.shortcuts import render

# Create your views here.
def index(request):
    p_title = "AFRO DJANGO TEMPLATING"
    user_name = "Brian Abura"
    gender = "Male"
    return render(request, 'index.html', {'p_title': p_title, 'user_name':user_name, 'gender': gender})

def register(request):
    return render(request, 'register.html')