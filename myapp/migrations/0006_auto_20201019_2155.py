# Generated by Django 3.1.2 on 2020-10-20 01:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20201019_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 20, 1, 55, 51, 275844, tzinfo=utc)),
        ),
    ]
