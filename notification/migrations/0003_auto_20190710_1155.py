# Generated by Django 2.2.1 on 2019-07-10 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20190703_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentfriendrequest',
            name='seen_notifications',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sentfriendrequest',
            name='seen_requests',
            field=models.BooleanField(default=False),
        ),
    ]