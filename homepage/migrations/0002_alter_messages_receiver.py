# Generated by Django 4.0.4 on 2022-05-14 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='receiver',
            field=models.CharField(max_length=15),
        ),
    ]
