# Generated by Django 2.2.2 on 2019-08-14 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0013_auto_20190813_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='FIRST_NAME',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='MIDDLE_NAME',
            field=models.CharField(blank=True, max_length=61, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='PHONE',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]