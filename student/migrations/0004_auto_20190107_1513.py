# Generated by Django 2.1.5 on 2019-01-07 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_deficit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='deficit',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]