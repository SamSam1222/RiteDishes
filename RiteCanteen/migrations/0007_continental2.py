# Generated by Django 4.1.7 on 2023-03-11 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RiteCanteen', '0006_rename_body2_continental_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Continental2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_uploaded')),
                ('title', models.CharField(max_length=250, null=True)),
                ('body', models.TextField(blank=True, max_length=500, null=True)),
                ('slug', models.SlugField()),
                ('created_on', models.DateTimeField(auto_now=True, null=True)),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
