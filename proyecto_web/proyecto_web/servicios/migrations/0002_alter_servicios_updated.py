# Generated by Django 5.0.2 on 2024-04-17 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
