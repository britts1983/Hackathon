# Generated by Django 2.2.2 on 2019-08-22 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0015_user_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='STATUS',
            field=models.CharField(blank=True, choices=[('Pending', 'PENDING'), ('Checking', 'CHECKING'), ('Approved', 'APPROVED'), ('Rejected', 'REJECTED')], default='pending', max_length=120, null=True),
        ),
    ]
