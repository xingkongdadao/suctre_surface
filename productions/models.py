# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import uuid
from datetime import timezone, datetime

from django.db import models


class Giay_san_xuat(models.Model):
    STT = models.UUIDField(default=uuid.uuid1, editable=False)
    MSC = models.CharField(primary_key=True, max_length=40)
    ngay_san_xuat = models.DateField(null=True, blank=True)
    ngay_nhap_kho = models.DateField(null=True, blank=True)
    so_may_xeo = models.CharField(max_length=10)
    CA = models.CharField(max_length=10)
    giay_loai = models.CharField(max_length=20)
    KL_san_xuat = models.FloatField(null=True, blank=True)
    KLKD = models.CharField(max_length=20)
    chat_luong = models.CharField(max_length=20)
    nguyen_nhan = models.CharField(max_length=50)
    giay_kho = models.IntegerField(null=True, blank=True)
    dinh_luong = models.IntegerField(null=True, blank=True)
    dinh_luong_T_te = models.IntegerField(null=True, blank=True)
    duong_kinh = models.IntegerField(null=True, blank=True)
    do_buc = models.CharField(max_length=20)
    do_am = models.CharField(max_length=20)
    C_tham = models.CharField(max_length=20)
    moi_noi = models.IntegerField(null=True, blank=True)
    ghi_chu = models.CharField(max_length=100)
    so_cong_ty = models.CharField(max_length=20)
    thoi_gian = models.CharField(max_length=20)
    nguoi_ghi_so = models.CharField(max_length=30)
    KCS = models.CharField(max_length=30)
    nguoi_lap_bang = models.CharField(max_length=30)
    tai_xe_kep = models.CharField(max_length=30)
    loai_nhap_kho = models.CharField(max_length=20)
    thoi_gian_bat_dau = models.DateTimeField(null=True, blank=True)
    thoi_gian_ket_thuoc = models.DateTimeField(null=True, blank=True)
    so_giay_lon = models.CharField(max_length=40)
    zhijing = models.IntegerField(null=True, blank=True)


class GiayNhapKho(models.Model):
    ngay_nhap_kho = models.DateField(null=True, blank=True)
    MSC = models.CharField(primary_key=True, max_length=40)

    def __str__(self):
        return self.MSC


