# Generated by Django 3.1.2 on 2020-10-20 16:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20201019_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 20, 16, 25, 48, 539389, tzinfo=utc)),
        ),
    ]
