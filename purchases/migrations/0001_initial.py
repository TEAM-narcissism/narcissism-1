# Generated by Django 2.2.5 on 2021-02-22 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='room_photos')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('closed', models.DateTimeField()),
                ('title', models.CharField(blank=True, max_length=40)),
                ('explain', models.TextField(blank=True)),
                ('max_people', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('address', models.CharField(blank=True, max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Immaterial',
            fields=[
                ('purchase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchases.Purchase')),
                ('category', models.CharField(choices=[('인터넷 서비스 공유', '인터넷 서비스 공유'), ('교육', '교육'), ('여가 활동', '여가 활동'), ('기타', '기타')], default='인터넷 서비스 공유', max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=('purchases.purchase',),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('purchase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchases.Purchase')),
                ('unit', models.CharField(blank=True, max_length=5)),
                ('link_address', models.URLField(blank=True)),
                ('category', models.CharField(choices=[('음식', '음식'), ('생필품', '생필품'), ('기타', '기타')], default='음식', max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=('purchases.purchase',),
        ),
    ]
