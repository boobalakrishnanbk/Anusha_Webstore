# Generated by Django 2.2.9 on 2020-04-19 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('salary', models.IntegerField()),
                ('manager', models.CharField(max_length=50)),
            ],
        ),
    ]
