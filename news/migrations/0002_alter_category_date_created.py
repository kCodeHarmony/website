# Generated by Django 4.0.3 on 2023-06-29 18:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 29, 18, 9, 33, 745762, tzinfo=utc)),
        ),
    ]