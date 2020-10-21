# Generated by Django 3.1.2 on 2020-10-19 23:31

import datetime
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='length',
            field=models.IntegerField(default=12),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('level', models.CharField(choices=[('HS', 'High School'), ('UG', 'Undergraduate'), ('PG', 'Postgraduate'), ('ND', 'No Degree')], default='HS', max_length=2)),
                ('address', models.CharField(max_length=300)),
                ('province', models.CharField(blank=True, default='ON', max_length=2)),
                ('interested_in', models.ManyToManyField(to='myapp.Topic')),
                ('registered_courses', models.ManyToManyField(blank=True, to='myapp.Course')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.IntegerField(choices=[(0, 'Cancelled'), (1, 'Confirmed'), (2, 'On Hold')], default=1, max_length=2)),
                ('order_date', models.DateField(default=datetime.datetime(2020, 10, 19, 23, 31, 3, 366344, tzinfo=utc))),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='myapp.student')),
                ('courses', models.ManyToManyField(to='myapp.Course')),
            ],
        ),
    ]