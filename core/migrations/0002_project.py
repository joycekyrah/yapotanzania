# Generated by Django 3.1 on 2021-11-21 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
                ('overview', models.CharField(max_length=250)),
                ('Percent', models.CharField(max_length=10)),
                ('raised_amount', models.CharField(max_length=20)),
                ('goal_amount', models.CharField(max_length=20)),
                ('sponsor', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
