# Generated by Django 5.0 on 2023-12-24 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laws', '0003_alter_administrativeoffencescodechapter_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrativeoffencescode',
            name='number',
            field=models.CharField(max_length=3, verbose_name='номер статьи'),
        ),
    ]