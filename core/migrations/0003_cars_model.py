# Generated by Django 4.2.6 on 2024-07-30 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cars_colour_cars_variant'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='model',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
