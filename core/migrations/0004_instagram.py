# Generated by Django 3.1 on 2021-11-21 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211121_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
    ]
