# Generated by Django 4.1.7 on 2023-03-10 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiteCanteen', '0002_pestrils_fruit_drink_continental'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='continental',
            name='body',
        ),
        migrations.RemoveField(
            model_name='continental',
            name='name',
        ),
        migrations.RemoveField(
            model_name='drink',
            name='body',
        ),
        migrations.RemoveField(
            model_name='drink',
            name='name',
        ),
        migrations.RemoveField(
            model_name='fruit',
            name='body',
        ),
        migrations.RemoveField(
            model_name='fruit',
            name='name',
        ),
        migrations.RemoveField(
            model_name='pestrils',
            name='body',
        ),
        migrations.RemoveField(
            model_name='pestrils',
            name='name',
        ),
        migrations.AlterField(
            model_name='continental',
            name='title',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
