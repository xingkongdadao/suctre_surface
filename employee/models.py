import uuid

from django.db import models


class Employee(models.Model):
    so_lam_viec = models.CharField(max_length=20, primary_key=True, editable=False)
    ho_ten = models.CharField(max_length=30)
    bo_phan = models.CharField(max_length=30)
    dien_thoai = models.CharField(max_length=20)
    thoi_gian_lam = models.DateField()
    thoi_gian_nghie_viec = models.DateField()

    def __str__(self):
        return self.ho_ten

