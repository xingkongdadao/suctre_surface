from django.urls import path

from . import views

urlpatterns = [
    path('', views.employee_information, name='employee_page'),
    path('<so_lam_viec>/', views.employee_one, name='employee_page'),

]
