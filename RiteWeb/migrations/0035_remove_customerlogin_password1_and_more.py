# Generated by Django 4.1.7 on 2023-11-25 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiteWeb', '0034_customerlogin_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerlogin',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='customerlogin',
            name='password2',
        ),
        migrations.AddField(
            model_name='customerlogin',
            name='password',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
