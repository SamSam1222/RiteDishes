# Generated by Django 4.1.7 on 2023-03-16 18:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RiteWeb', '0015_rename_food_food2'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Food2',
            new_name='Food',
        ),
    ]
