# Generated by Django 4.2.5 on 2023-11-26 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoreactapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]