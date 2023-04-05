# Generated by Django 4.1.7 on 2023-03-12 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RiteCanteen', '0008_remove_comment_rite_comment_love'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='love',
        ),
        migrations.AddField(
            model_name='comment',
            name='rite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='RiteCanteen.continental'),
        ),
    ]
