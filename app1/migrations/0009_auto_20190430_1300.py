# Generated by Django 2.1.4 on 2019-04-30 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20190430_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='time',
            field=models.DurationField(default=0),
        ),
    ]
