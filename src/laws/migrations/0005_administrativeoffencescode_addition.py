# Generated by Django 5.0 on 2023-12-24 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laws', '0004_alter_administrativeoffencescode_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrativeoffencescode',
            name='addition',
            field=models.TextField(blank=True, null=True, verbose_name='дополнение'),
        ),
    ]
