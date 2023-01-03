# Generated by Django 4.1.5 on 2023-01-03 13:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostUser',
            fields=[
                ('userId', models.IntegerField(primary_key=True, serialize=False)),
                ('userPass', models.CharField(max_length=20)),
                ('upload_date', models.DateTimeField(default=datetime.timezone)),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/')),
            ],
        ),
    ]
