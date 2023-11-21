# Generated by Django 4.2.7 on 2023-11-20 16:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('corpLearnApp', '0008_alter_employeecourse_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeecourse',
            name='deadline',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='employeecourse',
            name='end_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='employeecourse',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]