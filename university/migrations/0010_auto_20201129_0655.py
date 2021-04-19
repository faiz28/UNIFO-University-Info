# Generated by Django 3.1.3 on 2020-11-29 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0009_auto_20201128_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='uni_cat',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='uni_cat',
            name='uni_category',
            field=models.CharField(default='', max_length=300, unique=True),
        ),
    ]
