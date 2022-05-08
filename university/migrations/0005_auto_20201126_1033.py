# Generated by Django 3.1.3 on 2020-11-26 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0004_auto_20201126_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='subject_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(default='', max_length=300, unique=True)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='department_list',
            name='department_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.subject_list'),
        ),
        migrations.DeleteModel(
            name='sub_list',
        ),
    ]