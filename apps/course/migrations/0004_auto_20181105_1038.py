# Generated by Django 2.0 on 2018-11-05 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20181028_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]