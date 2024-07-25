from django.shortcuts import render
from .models import Employee


def homePageView(request):
    employees = Employee.objects.filter(about='Test')
    return render(request, 'list.html', {'employees': employees})