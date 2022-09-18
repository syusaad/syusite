# Generated by Django 4.1.1 on 2022-09-18 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Response',
                'verbose_name_plural': 'Responses',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=255)),
                ('client', models.CharField(max_length=255)),
                ('startDate', models.DateField(default=datetime.date.today, verbose_name='Project Start Date')),
                ('endDate', models.DateField(default=datetime.date.today, verbose_name='Project End Date')),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Previous Projects',
            },
        ),
    ]
