# Generated by Django 4.1.13 on 2024-12-06 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_hydjobs_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hydjobs',
            name='address',
            field=models.CharField(max_length=250),
        ),
    ]
