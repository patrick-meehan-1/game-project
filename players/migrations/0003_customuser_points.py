# Generated by Django 4.2.1 on 2023-12-18 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_alter_customuser_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='points',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
