# Generated by Django 2.2.5 on 2021-02-22 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('purchases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='purchase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='purchases.Purchase'),
        ),
    ]
