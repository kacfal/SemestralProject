# Generated by Django 2.1.5 on 2019-01-05 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='index',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.TextField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=10),
        ),
    ]
