# Generated by Django 3.1 on 2020-12-03 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20201203_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_info',
            name='uni_name',
            field=models.CharField(default='u', max_length=500),
        ),
    ]
