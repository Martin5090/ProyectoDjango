from django.shortcuts import render
from .models import Zapatilla

def index(request):
    zapatillas= Zapatilla.objects.all()
    context={"zapatillas":zapatillas}
    return render(request, 'zapatillasweb/index.html', context)

def login_view(request):
    return render(request, 'zapatillasweb/login.html')

def home(request):
    return render(request, 'zapatillasweb/home.html')