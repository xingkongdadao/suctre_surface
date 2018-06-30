from django.shortcuts import render

from employee import models


def employee_information(request):
    employee_all = models.Employee.objects.all()
    return render(request, "employee/employee_show.html", {'employee_all': employee_all})


def employee_one(request, so_lam_viec):
    employee_one = models.Employee.objects.get(so_lam_viec=so_lam_viec)
    return render(request, 'employee/so_lam_viec.html', {'employee_one': employee_one})
