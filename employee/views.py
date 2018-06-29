from django.shortcuts import render

from employee import models


def employee_information(request):
    employee_all = models.Employee.objects.all()
    return render(request, "employee/employee_show.html", {'employee_all': employee_all})
