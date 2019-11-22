# Generated by Django 2.2.6 on 2019-11-16 09:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('remark', models.TextField(blank=True, max_length=255)),
                ('class_scheduled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=9)),
                ('section', models.CharField(choices=[('1A', 'Class 1/2/3 Section-A'), ('1B', 'Class 1/2/3 Section-B'), ('1C', 'Class 1/2/3 Section-C'), ('1I', 'Class 1/2/3 Irregular'), ('2A', 'Class 4/5 Section-A'), ('2B', 'Class 4/5 Section-B'), ('2C', 'Class 4/5 Section-C'), ('2I', 'Class 4/5 Irregular'), ('3A', 'Class 6/7/8 Section-A'), ('3B', 'Class 6/7/8 Section-B'), ('3C', 'Class 6/7/8 Section-C'), ('3I', 'Class 6/7/8 Irregular'), ('4A', 'Class 9'), ('4B', 'Class 10'), ('NA', 'Navodaya A'), ('NB', 'Navodaya B'), ('NC', 'Navodaya C')], max_length=2)),
                ('subject', models.CharField(choices=[('eng', 'English'), ('hin', 'Hindi'), ('mat', 'Mathematics'), ('sci', 'Science')], default='hin', max_length=3)),
            ],
            options={
                'unique_together': {('day', 'section')},
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('school_class', models.CharField(max_length=2)),
                ('village', models.CharField(choices=[('G', 'Gadheri'), ('M', 'Mehgawan'), ('C', 'Chanditola'), ('A', 'Amanala'), ('S', 'Suarkol')], default='Gadheri', max_length=30)),
                ('contact_no', models.CharField(max_length=10)),
                ('guardian_name', models.CharField(max_length=30)),
                ('restricted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('roll_no', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True, verbose_name='Roll Number')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last name')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1)),
                ('batch', models.IntegerField(choices=[(2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015)])),
                ('programme', models.CharField(choices=[('bt', 'B.Tech'), ('mt', 'M.Tech'), ('phd', 'phD'), ('bd', 'B.Des'), ('md', 'M.Des')], max_length=2)),
                ('dob', models.DateField(default=datetime.datetime.now, verbose_name='Date of Birth')),
                ('contact_no', models.CharField(max_length=10, verbose_name='Contact Number')),
                ('street_address1', models.CharField(max_length=255, verbose_name='Address Line 1')),
                ('street_address2', models.CharField(max_length=255, verbose_name='Address Line 2')),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=25)),
                ('pincode', models.CharField(max_length=6)),
                ('alt_email', models.EmailField(max_length=255, unique=True, verbose_name='Alternate Email')),
                ('desig', models.CharField(choices=[('Co-Convenor', (('mcoco', 'Math Co-Convenor'), ('ecoco', 'English Co-Convenor'), ('hcoco', 'Hindi Co-Convenor'))), ('Convenor', (('mco', 'Math Convenor'), ('eco', 'English Convenor'), ('hco', 'Hindi Convenor'))), ('jac', 'Jagrati Advisory Commitee'), ('v', 'Volunteer')], default='v', max_length=5, verbose_name='Designation')),
                ('active', models.BooleanField(default=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer_schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, max_length=10)),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Volunteer')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Schedule')),
            ],
            options={
                'unique_together': {('roll_no', 'day')},
            },
        ),
        migrations.CreateModel(
            name='Volunteer_attended_on',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Calendar')),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Volunteer')),
            ],
            options={
                'unique_together': {('roll_no', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Student_schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, max_length=10)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Schedule')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Student')),
            ],
            options={
                'unique_together': {('sid', 'day')},
            },
        ),
        migrations.CreateModel(
            name='Student_attended_on',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hw_dome', models.BooleanField(default=False)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Calendar')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Student')),
            ],
            options={
                'unique_together': {('sid', 'date')},
            },
        ),
        migrations.CreateModel(
            name='cw_hw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cw', models.TextField(max_length=255)),
                ('hw', models.TextField(max_length=255)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Calendar')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Schedule')),
            ],
            options={
                'unique_together': {('date', 'section')},
            },
        ),
    ]
