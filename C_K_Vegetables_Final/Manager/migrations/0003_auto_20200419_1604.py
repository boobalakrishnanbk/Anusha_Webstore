# Generated by Django 2.2.9 on 2020-04-19 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0002_employee_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_attendance',
            name='designation',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee_attendance',
            name='locality',
            field=models.CharField(default='ed', max_length=50),
            preserve_default=False,
        ),
    ]