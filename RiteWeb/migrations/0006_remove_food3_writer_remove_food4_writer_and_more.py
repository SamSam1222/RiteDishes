# Generated by Django 4.1.7 on 2023-03-02 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RiteWeb', '0005_food8_food7_food6_food5_food4_food3_food2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food3',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='food4',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='food5',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='food6',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='food7',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='food8',
            name='writer',
        ),
        migrations.DeleteModel(
            name='Food2',
        ),
        migrations.DeleteModel(
            name='Food3',
        ),
        migrations.DeleteModel(
            name='Food4',
        ),
        migrations.DeleteModel(
            name='Food5',
        ),
        migrations.DeleteModel(
            name='Food6',
        ),
        migrations.DeleteModel(
            name='Food7',
        ),
        migrations.DeleteModel(
            name='Food8',
        ),
    ]
