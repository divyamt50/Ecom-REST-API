# Generated by Django 4.1.6 on 2023-07-06 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_category_otp_category_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='otp',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]