# Generated by Django 4.1.7 on 2023-11-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiteWeb', '0047_remove_user_password_userprofileinfo_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='username',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
    ]
