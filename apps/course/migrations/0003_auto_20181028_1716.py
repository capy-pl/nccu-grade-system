# Generated by Django 2.0 on 2018-10-28 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
