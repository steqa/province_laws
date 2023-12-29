# Generated by Django 5.0 on 2023-12-29 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laws', '0007_alter_administrativeoffencescode_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='CriminalCodeChapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField(verbose_name='номер главы')),
                ('name', models.TextField(verbose_name='название')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата последнего обновления')),
            ],
        ),
        migrations.AlterField(
            model_name='administrativeoffencescode',
            name='arrest',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='срок ареста'),
        ),
        migrations.AlterField(
            model_name='administrativeoffencescode',
            name='deprivation_driver_license',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='срок лишение ВУ'),
        ),
        migrations.AlterField(
            model_name='administrativeoffencescode',
            name='penalty',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='сумма штрафа'),
        ),
        migrations.CreateModel(
            name='CriminalCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField(verbose_name='номер статьи')),
                ('text', models.TextField(verbose_name='текст')),
                ('penalty', models.CharField(blank=True, max_length=300, null=True, verbose_name='сумма штрафа')),
                ('conjunction_2', models.CharField(blank=True, choices=[('OR', 'или'), ('AND', 'и')], max_length=3, null=True, verbose_name='союз')),
                ('arrest', models.CharField(blank=True, max_length=300, null=True, verbose_name='срок ареста')),
                ('addition', models.TextField(blank=True, null=True, verbose_name='дополнение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата последнего обновления')),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chapter', to='laws.criminalcodechapter', verbose_name='глава')),
            ],
        ),
    ]
