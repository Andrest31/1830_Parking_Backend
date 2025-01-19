from django.shortcuts import render

def HelloPage(request):
    return render(request, 'HelloPage.html')

def MainPage(request):
    return render(request, 'MainPage.html')

def ParkingPage(request):
    return render(request, 'ParkingPage.html')

def PassPage(request):
    return render(request, 'PassPage.html')
