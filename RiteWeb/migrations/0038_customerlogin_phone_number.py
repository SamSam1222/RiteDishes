# Generated by Django 4.1.7 on 2023-11-25 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiteWeb', '0037_remove_customerlogin_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerlogin',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]