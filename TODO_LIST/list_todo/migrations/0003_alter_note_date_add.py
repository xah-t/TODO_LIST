# Generated by Django 3.2 on 2021-04-15 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_todo', '0002_auto_20210414_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date_add',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 16, 12, 45, 17, 82429)),
        ),
    ]
