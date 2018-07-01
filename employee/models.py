import uuid

from django.db import models


class LoaiLam(models.Model):
    STT = models.UUIDField(default=uuid.uuid1, editable=False)
    loai_lam = models.CharField(primary_key=True, max_length=20)
    gio_quy_dinh_di_lam = models.DateTimeField()
    gio_quy_dinh_tan_lam = models.DateTimeField()
    ghi_chu = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.loai_lam


class Department(models.Model):
    STT = models.UUIDField(default=uuid.uuid1, editable=False)
    department = models.CharField(primary_key=True, max_length=50)
    ghi_chu = models.CharField(max_length=50)


class Employee(models.Model):
    so_lam_viec = models.CharField(max_length=20, primary_key=True, editable=False)
    ho_va_ten = models.CharField(max_length=30)
    bo_phan = models.CharField(max_length=30, blank=True)
    bo_phan_cu_the = models.CharField(max_length=30, blank=True)
    chuc_vu = models.CharField(max_length=30, blank=True)
    gioi_tinh = models.CharField(max_length=10, blank=True)
    trang_thai = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    skype = models.CharField(max_length=20, blank=True)
    dien_thoai = models.CharField(max_length=20, blank=True)
    dien_thoai_2 = models.CharField(max_length=20, blank=True)
    CMND = models.CharField(max_length=20, blank=True)
    highest_education = models.CharField(max_length=100, blank=True)
    nhi_chu = models.CharField(max_length=100, blank=True)
    ngay_sinh = models.DateField(blank=True, null=True)
    ngay_vao_cong_ty = models.DateField(blank=True, null=True)
    ngay_ra_cong_ty = models.DateField(blank=True, null=True)
    tinh = models.CharField(max_length=20, blank=True)
    thanh_pho = models.CharField(max_length=20, blank=True)
    quan_huyen = models.CharField(max_length=20, blank=True)
    phuong_xa = models.CharField(max_length=20, blank=True)
    dia_chi_cu_the = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.ho_va_ten


class PhanCongCongViec(models.Model):
    STT = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    ngay_lam = models.DateField()
    loai_lam = models.ForeignKey(LoaiLam, on_delete=models.CASCADE, )
    trang_thai = models.CharField(max_length=20)
    so_lam_viec = models.ForeignKey(Employee, on_delete=models.CASCADE)
    thoi_gian_di_lam = models.DateTimeField(null=True, blank=True)
    thoi_gian_tan_lam = models.DateTimeField(null=True, blank=True)
    ghi_chu = models.CharField(max_length=50)

    def __str__(self):
        return self.so_lam_viec
