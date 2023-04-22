from django.shortcuts import render

# Create your views here.
def index(request):
    p_title = "AFRO DJANGO TEMPLATING"
    s_title = "Links"
    return render(request, 'index.html', {'p_title': p_title, 's_title':s_title})