# Generated by Django 4.0.2 on 2022-05-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_bio_user_education_user_eligibility_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='', height_field=224, null=True, upload_to='Profile', width_field=225),
        ),
    ]
