# Generated by Django 5.0 on 2023-12-24 07:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laws', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrativeOffencesCodeChapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField(verbose_name='номер главы')),
                ('name', models.TextField(verbose_name='название')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата последнего обновления')),
            ],
        ),
        migrations.AlterField(
            model_name='administrativeoffencescode',
            name='conjunction_1',
            field=models.CharField(blank=True, choices=[('OR', 'или'), ('AND', 'и')], max_length=3, null=True, verbose_name='союз'),
        ),
        migrations.AlterField(
            model_name='administrativeoffencescode',
            name='conjunction_2',
            field=models.CharField(blank=True, choices=[('OR', 'или'), ('AND', 'и')], max_length=3, null=True, verbose_name='союз'),
        ),
        migrations.AlterField(
            model_name='administrativeoffencescode',
            name='conjunction_3',
            field=models.CharField(blank=True, choices=[('OR', 'или'), ('AND', 'и')], max_length=3, null=True, verbose_name='союз'),
        ),
        migrations.AddField(
            model_name='administrativeoffencescode',
            name='chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chapter', to='laws.administrativeoffencescodechapter', verbose_name='глава'),
        ),
    ]