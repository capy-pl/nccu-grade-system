# Generated by Django 2.0 on 2018-08-30 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='leave_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='registered_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
