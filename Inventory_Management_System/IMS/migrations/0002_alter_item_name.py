# Generated by Django 5.0.4 on 2024-05-19 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]