# Generated by Django 4.1.13 on 2024-12-06 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hydjobs',
            name='address',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
