# Generated by Django 2.1.4 on 2019-05-17 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_auto_20190517_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='time',
        ),
    ]
