# Generated by Django 2.1.4 on 2019-05-30 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='date_of_finish',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='date_of_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
