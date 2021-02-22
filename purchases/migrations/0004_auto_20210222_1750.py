# Generated by Django 2.2.5 on 2021-02-22 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0003_purchase_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.CharField(choices=[('진행 중', '진행 중'), ('모집 완료', '모집 완료'), ('기간 만료', '기간 만료'), ('거래 완료', '거래 완료')], default='진행 중', max_length=16),
        ),
    ]
