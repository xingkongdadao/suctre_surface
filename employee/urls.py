from django.urls import path

from . import views

urlpatterns = [
    path('', views.employee_information, name='employee_information'),

]
