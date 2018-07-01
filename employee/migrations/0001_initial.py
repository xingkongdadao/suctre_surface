# Generated by Django 2.0.6 on 2018-07-02 00:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('STT', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('department', models.CharField(max_length=50, unique=True, verbose_name='bộ phần')),
                ('department_cn', models.CharField(blank=True, max_length=50, null=True, verbose_name='部门')),
                ('ghi_chu', models.CharField(blank=True, max_length=50, verbose_name='ghi chú')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('so_lam_viec', models.CharField(editable=False, max_length=20, primary_key=True, serialize=False)),
                ('ho_va_ten', models.CharField(max_length=30)),
                ('bo_phan_cu_the', models.CharField(blank=True, max_length=30)),
                ('chuc_vu', models.CharField(blank=True, max_length=30)),
                ('gioi_tinh', models.CharField(blank=True, max_length=10)),
                ('trang_thai', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('skype', models.CharField(blank=True, max_length=20)),
                ('dien_thoai', models.CharField(blank=True, max_length=20)),
                ('dien_thoai_2', models.CharField(blank=True, max_length=20)),
                ('CMND', models.CharField(blank=True, max_length=20)),
                ('highest_education', models.CharField(blank=True, max_length=100)),
                ('nhi_chu', models.CharField(blank=True, max_length=100)),
                ('ngay_sinh', models.DateField(blank=True, null=True)),
                ('ngay_vao_cong_ty', models.DateField(blank=True, null=True)),
                ('ngay_ra_cong_ty', models.DateField(blank=True, null=True)),
                ('tinh', models.CharField(blank=True, max_length=20)),
                ('thanh_pho', models.CharField(blank=True, max_length=20)),
                ('quan_huyen', models.CharField(blank=True, max_length=20)),
                ('phuong_xa', models.CharField(blank=True, max_length=20)),
                ('dia_chi_cu_the', models.CharField(blank=True, max_length=60)),
                ('bo_phan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Department')),
            ],
        ),
        migrations.CreateModel(
            name='LoaiLam',
            fields=[
                ('STT', models.UUIDField(default=uuid.uuid1, editable=False)),
                ('loai_lam', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='loài làm')),
                ('gio_quy_dinh_di_lam', models.DateTimeField(verbose_name='giờ quy đình đi làm')),
                ('gio_quy_dinh_tan_lam', models.DateTimeField(verbose_name='giờ quy đinh tan làm')),
                ('ghi_chu', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PhanCongCongViec',
            fields=[
                ('STT', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('ngay_lam', models.DateField()),
                ('trang_thai', models.CharField(max_length=20)),
                ('thoi_gian_di_lam', models.DateTimeField(blank=True, null=True)),
                ('thoi_gian_tan_lam', models.DateTimeField(blank=True, null=True)),
                ('ghi_chu', models.CharField(max_length=50)),
                ('loai_lam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.LoaiLam')),
                ('so_lam_viec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
        ),
    ]
