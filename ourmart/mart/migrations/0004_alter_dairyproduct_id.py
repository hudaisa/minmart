# Generated by Django 4.0.5 on 2022-07-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0003_beverages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dairyproduct',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]