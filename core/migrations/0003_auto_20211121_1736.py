# Generated by Django 3.1 on 2021-11-21 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='Percent',
            new_name='percent',
        ),
    ]
