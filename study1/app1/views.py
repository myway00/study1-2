from django.shortcuts import render
def home(request):
    return render(request, "home.html")

def result(request):
    userName =  request.GET['name']
    return render(request, "result.html",{"userName" : userName}) #키 : 값