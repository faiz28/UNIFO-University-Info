# Generated by Django 3.1.3 on 2020-11-28 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20201128_0320'),
        ('university', '0007_achievment_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievment_list',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.userinfo'),
        ),
    ]