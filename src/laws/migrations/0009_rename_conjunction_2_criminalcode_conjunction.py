# Generated by Django 5.0 on 2023-12-29 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laws', '0008_criminalcodechapter_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='criminalcode',
            old_name='conjunction_2',
            new_name='conjunction',
        ),
    ]
