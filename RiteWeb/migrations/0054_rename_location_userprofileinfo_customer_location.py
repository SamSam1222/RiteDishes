# Generated by Django 4.1.7 on 2023-11-30 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RiteWeb', '0053_remove_userprofileinfo_password_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='location',
            new_name='Customer_location',
        ),
    ]
