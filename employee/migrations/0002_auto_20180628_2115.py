# Generated by Django 2.0.6 on 2018-06-28 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_modify_date',
        ),
    ]
