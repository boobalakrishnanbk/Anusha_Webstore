# Generated by Django 2.2.9 on 2020-04-19 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0004_auto_20200419_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_attendance',
            name='designation',
            field=models.CharField(max_length=50),
        ),
    ]
