# Generated by Django 4.2.1 on 2023-12-18 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_alter_season_memory_wall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='memory_wall',
        ),
        migrations.AlterField(
            model_name='season',
            name='poster',
            field=models.ImageField(null=True, upload_to='season_posters/'),
        ),
    ]
