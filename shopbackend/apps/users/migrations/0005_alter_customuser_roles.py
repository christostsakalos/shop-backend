# Generated by Django 3.2.2 on 2021-05-17 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='roles',
            field=models.CharField(choices=[('Staff', 'Staff'), ('User', 'User')], default='User', max_length=50, null=True),
        ),
    ]
