# Generated by Django 2.0.6 on 2018-06-25 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='问题',
        ),
    ]