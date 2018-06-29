from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from employee import models


def index(request):
    return HttpResponse("Hello,人员信息组建公司电脑 !!!.")


def employee_information(request):
    employee_all = models.Employee.objects.all()
    return render(request, "employee_show.html", {'employee_all': employee_all})
