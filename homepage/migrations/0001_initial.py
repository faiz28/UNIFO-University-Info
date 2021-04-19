# Generated by Django 3.1 on 2020-11-20 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default=0)),
                ('university_category', models.CharField(max_length=5000)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]