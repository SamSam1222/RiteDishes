# Generated by Django 4.1.7 on 2023-11-21 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiteWeb', '0028_location_body2_location_body3_location_body4_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]