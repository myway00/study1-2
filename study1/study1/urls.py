
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"), #name을 씀으로써 url을 저 name으로 대체가능
    path('result/', views.result, name="result"),
    path('about/', views.about, name="about"),
]
