# Generated by Django 2.2.5 on 2021-02-14 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210212_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='qr_code',
            field=models.FileField(blank=True, upload_to='qr_codes'),
        ),
    ]
