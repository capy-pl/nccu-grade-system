# Generated by Django 2.0 on 2018-08-29 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('cellphone_number', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('registered_date', models.DateField(blank=True)),
                ('leave_date', models.DateField(blank=True)),
                ('year_in_school', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
