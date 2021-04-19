# Generated by Django 3.1.3 on 2020-11-26 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unilist',
            name='uni_category',
            field=models.CharField(choices=[('RU', 'University of Rajshahi'), ('DU', 'University of Dhaka'), ('CU', 'University of Chitagong'), ('KU', 'University of Khulna')], default='', max_length=300),
        ),
    ]