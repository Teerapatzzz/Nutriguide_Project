from django.shortcuts import render
from . models import foodtable
from .forms import FoodInfoForm
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def allMenu(request):
    foods = foodtable.objects.all()
    return render(request, 'app_food/allMenu.html', {'foods': foods})

@login_required
def addMenu(request):
    if request.method == 'POST':
        form = FoodInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # ทำสิ่งที่คุณต้องการหลังจากบันทึกข้อมูล
    else:
        form = FoodInfoForm()

    context = {'form': form}
    return render(request, 'app_food/addMenu.html', context)
