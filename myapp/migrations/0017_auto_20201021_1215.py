# Generated by Django 3.1.2 on 2020-10-21 16:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20201020_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 21, 16, 15, 19, 484104, tzinfo=utc)),
        ),
    ]
