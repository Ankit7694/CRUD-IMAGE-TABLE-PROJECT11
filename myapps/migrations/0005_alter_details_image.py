# Generated by Django 5.0 on 2023-12-07 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0004_details_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='image',
            field=models.ImageField(default='', upload_to='static/images'),
        ),
    ]
