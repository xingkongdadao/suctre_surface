from django.contrib import admin

# Register your models here.
from employee.models import *

admin.site.register(Employee)
admin.site.register(LoaiLam)
admin.site.register(PhanCongCongViec)
