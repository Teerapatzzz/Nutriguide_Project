from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'app_general/home.html')

def about(reguest):
    return render(reguest,'app_general/about.html')