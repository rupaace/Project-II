# Generated by Django 4.0.2 on 2022-05-16 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0011_alter_job_last_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='last_date',
            field=models.DateTimeField(),
        ),
    ]