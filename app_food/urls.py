from django.urls import path,include
from . import views

urlpatterns = [
    path('allMenu',views.allMenu,name='allMenu'),
    path('addMenu',views.addMenu,name='addMenu'),
]
