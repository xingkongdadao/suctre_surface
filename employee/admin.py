from django.contrib import admin

# Register your models here.
from employee.models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('so_lam_viec', 'ho_va_ten', 'bo_phan')
    search_fields = ('so_lam_viec', 'ho_va_ten')


class LoaiLamAdmin(admin.ModelAdmin):
    list_display = ('loai_lam', 'gio_quy_dinh_di_lam', 'gio_quy_dinh_tan_lam')


class PhanCongCongViecAdmin(admin.ModelAdmin):
    list_display = ('ngay_lam', 'loai_lam', 'so_lam_viec', 'trang_thai', 'thoi_gian_di_lam', 'thoi_gian_tan_lam')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(LoaiLam, LoaiLamAdmin)
admin.site.register(PhanCongCongViec, PhanCongCongViecAdmin)
