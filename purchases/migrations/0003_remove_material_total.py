# Generated by Django 2.2.5 on 2021-02-19 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0002_auto_20210218_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='total',
        ),
    ]
