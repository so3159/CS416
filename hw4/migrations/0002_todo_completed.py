# Generated by Django 3.2.9 on 2021-11-30 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw4', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
