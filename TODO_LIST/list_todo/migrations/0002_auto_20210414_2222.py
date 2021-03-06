# Generated by Django 3.2 on 2021-04-14 19:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='nlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='note',
            name='date_add',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 15, 22, 22, 6, 535167)),
        ),
        migrations.AlterField(
            model_name='note',
            name='note_status',
            field=models.IntegerField(choices=[(0, 'Активно'), (1, 'Ожидание'), (2, 'Выполнено')], default=0, verbose_name='Статус дела'),
        ),
    ]
