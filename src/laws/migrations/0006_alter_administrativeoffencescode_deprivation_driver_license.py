# Generated by Django 5.0 on 2023-12-24 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laws', '0005_administrativeoffencescode_addition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrativeoffencescode',
            name='deprivation_driver_license',
            field=models.CharField(blank=True, max_length=41, null=True, verbose_name='срок лишение ВУ'),
        ),
    ]
